#!/usr/bin/env python3

import json
import subprocess
import sys
import threading
from datetime import datetime
from pathlib import Path

STATE = Path("/tmp/i3_per_output_ws_history.json")
LOG = Path("/tmp/i3_per_output_alt_tab.log")

lock = threading.Lock()


def log(msg):
    ts = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    LOG.write_text(LOG.read_text() + line + "\n" if LOG.exists() else line + "\n")


def i3_cmd(cmd):
    log(f"i3-msg: {cmd}")
    subprocess.run(
        ["i3-msg"] + cmd.split(),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def load_state():
    if not STATE.exists():
        return {}
    try:
        return json.loads(STATE.read_text())
    except Exception:
        return {}


def save_state(state):
    STATE.write_text(json.dumps(state))


def get_focused_output():
    tree = json.loads(subprocess.check_output(["i3-msg", "-t", "get_tree"]))

    def walk(n):
        if n.get("focused"):
            return n
        for k in ("nodes", "floating_nodes"):
            for c in n.get(k, []):
                r = walk(c)
                if r:
                    return r
        return None

    node = walk(tree)
    out = node["output"]
    log(f"Focused output: {out}")
    return out


def subscribe():
    log("Starting workspace focus listener")

    state = load_state()

    p = subprocess.Popen(
        ["i3-msg", "-t", "subscribe", "-m", '[ "workspace" ]'],
        stdout=subprocess.PIPE,
        text=True,
    )

    for line in p.stdout:
        event = json.loads(line)
        if event.get("change") != "focus":
            continue

        ws = event.get("current")
        if not ws:
            continue

        output = ws["output"]
        name = ws["name"]

        with lock:
            cur, prev = state.get(output, (None, None))
            if name != cur:
                state[output] = (name, cur)
                save_state(state)
                log(f"Update [{output}]: cur={name}, prev={cur}")


def alt_tab():
    log("Alt+Tab triggered")

    state = load_state()
    output = get_focused_output()

    cur, prev = state.get(output, (None, None))
    log(f"History [{output}]: cur={cur}, prev={prev}")

    if prev:
        i3_cmd(f'workspace "{prev}"')
    else:
        log("No previous workspace for this output")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "alt-tab":
        alt_tab()
    else:
        subscribe()
