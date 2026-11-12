#!/bin/bash

# killall -q polybar

# while pgrep -u $UID -x polybar >/dev/null; do sleep 0.5; done

# polybar -c ~/Software/esta_base/configs/P520_arch/polybar_config.ini dp-bottom &
# polybar -c ~/Software/esta_base/configs/P520_arch/polybar_config.ini hdmi-top &
# polybar -c ~/Software/esta_base/configs/P520_arch/polybar_config.ini hdmi-bot &


# Monitor names
export MONITOR1="DP-3"
export MONITOR2="HDMI-1"

CONFIG="$HOME/Software/esta_base/configs/P520_arch/polybar_config.ini"

# Stop existing bars
killall -q polybar

while pgrep -u "$UID" -x polybar >/dev/null; do
    sleep 0.5
done

# Main monitor
polybar -c "$CONFIG" dp-bottom &

# Secondary monitor
polybar -c "$CONFIG" hdmi-top &
polybar -c "$CONFIG" hdmi-bot &