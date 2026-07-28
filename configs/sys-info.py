#!/usr/bin/env python3
# made from chip-temp.py
# in file: /home/ab/Software/esta_base/configs/sys-info.py
import subprocess
import re


def sh(cmd: str) -> str:
    return subprocess.check_output(
        cmd, shell=True, text=True, stderr=subprocess.STDOUT
    )


# ----------------- Temps -----------------

TEMP_RE = re.compile(r"[\+\-]?\d+(\.\d+)?°C")


def extract_temp(block: str) -> str:
    m = TEMP_RE.search(block)
    return m.group(0) if m else "N/A"


def get_temps():
    blocks = sh("sensors").split("\n\n")

    cpu_blocks = ("k10temp", "coretemp")
    gpu_blocks = ("amdgpu",)

    cpu_block = gpu_block = None

    for block in blocks:
        header = block.split("\n", 1)[0]
        if cpu_block is None and any(k in header for k in cpu_blocks):
            cpu_block = block
        if gpu_block is None and any(k in header for k in gpu_blocks):
            gpu_block = block

    return (
        extract_temp(cpu_block) if cpu_block else "N/A",
        extract_temp(gpu_block) if gpu_block else "N/A",
    )


# ----------------- Memory -----------------

def meminfo():
    info = {}
    with open("/proc/meminfo") as f:
        for line in f:
            k, v = line.split(":", 1)
            info[k] = int(v.strip().split()[0])  # kB
    return info


def swap_and_zram():
    """
    Returns:
      swap = {"used": bytes, "size": bytes}
      zram = {"used": bytes, "size": bytes} or None
    """
    try:
        out = sh("swapon --show --noheadings --bytes")
    except subprocess.CalledProcessError:
        return {"used": 0, "size": 0}, None

    swap = {"used": 0, "size": 0}
    zram = None

    for line in out.strip().splitlines():
        name, _, size, used, *_ = line.split()
        size = int(size)
        used = int(used)

        if name == "/swapfile":
            swap["size"] = size
            swap["used"] = used
        elif name.startswith("/dev/zram"):
            zram = {"size": size, "used": used}

    return swap, zram


# ----------------- Formatting -----------------

def gib_from_kb(kb: int) -> str:
    return f"{kb / 1024**2:.1f}G"


def gib_from_bytes(b: int) -> str:
    return f"{b / 1024**3:.1f}G"

def temp_int(t: str) -> str:
    if t == "N/A":
        return "NA"
    m = re.search(r"(-?\d+(\.\d+)?)", t)
    return str(int(float(m.group(1)))) if m else "NA"


def bar(used_g, total_g, scheme=2):
    if scheme==1:
        filled="█"
        empty="▒"
    if scheme==2:
        filled="⚫"
        empty="⚪"
        filled="■"
        empty="□"


    used = int(round(used_g))
    total = int(round(total_g))
    used = min(used, total)
    return filled * used + empty * (total - used)


def kb_to_gib(kb):
    return kb / 1024**2


def bytes_to_gib(b):
    return b / 1024**3


# ----------------- Main -----------------

def main():
    cpu_temp, gpu_temp = get_temps()

    mi = meminfo()
    mem_used = mi["MemTotal"] - mi["MemAvailable"]
    mem_total = mi["MemTotal"]

    swap, zram = swap_and_zram()

    parts = [
        f"cpu:{cpu_temp}",
        f"gpu:{gpu_temp}",
        f"ram:{gib_from_kb(mem_used)}/{gib_from_kb(mem_total)}",
        f"swap:{gib_from_bytes(swap['used'])}/{gib_from_bytes(swap['size'])}",
    ]

    if zram:
        parts.append(
            f"zram:{gib_from_bytes(zram['used'])}/{gib_from_bytes(zram['size'])}"
        )
    else:
        parts.append("zram:N/A")

    print(", ".join(parts))

def progress_bar():
    cpu_temp, gpu_temp = get_temps()
    cpu = temp_int(cpu_temp)
    gpu = temp_int(gpu_temp)

    mi = meminfo()
    mem_used_g = kb_to_gib(mi["MemTotal"] - mi["MemAvailable"])
    mem_total_g = kb_to_gib(mi["MemTotal"])

    swap, zram = swap_and_zram()

    swap_used_g = bytes_to_gib(swap["used"])
    swap_total_g = bytes_to_gib(swap["size"])

    # parts = [
    #     f"cpu:{cpu}",
    #     f"gpu:{gpu}",
    #     f"ram:{bar(mem_used_g, mem_total_g)}",
    #     f"swap:{bar(swap_used_g, swap_total_g)}",
    # ]

    parts = [
        f"CPU[{cpu}]",
        f"GPU[{gpu}]",
        f"RAM[{bar(mem_used_g, mem_total_g)}]",
        f"SWAP[{bar(swap_used_g, swap_total_g)}]",
    ]

    if zram:
        zram_used_g = bytes_to_gib(zram["used"])
        zram_total_g = bytes_to_gib(zram["size"])
        parts.append(f"ZRAM[{bar(zram_used_g, zram_total_g)}]")
    else:
        parts.append("zram:N/A")

    # print('( ◕͊‿◕͊ )',end='')
    print(", ".join(parts))


if __name__ == "__main__":
    # main()
    progress_bar()




