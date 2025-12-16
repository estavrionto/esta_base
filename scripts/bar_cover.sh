#!/bin/bash
PIDFILE=/tmp/screen_patches.pid

# If patches are already running, kill them
if [ -f "$PIDFILE" ]; then
    while read -r pid; do
        kill "$pid" 2>/dev/null
    done < "$PIDFILE"
    rm "$PIDFILE"
    exit 0
fi

# Otherwise, launch patches
# (examples, add as many as you want)
feh --geometry 300x150+100+200 --borderless --no-fehbg patch.png &
echo $! >> "$PIDFILE"

feh --geometry 250x100+600+400 --borderless --no-fehbg patch.png &
echo $! >> "$PIDFILE"
