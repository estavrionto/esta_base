#!/bin/bash

killall -q polybar

while pgrep -u $UID -x polybar >/dev/null; do sleep 0.5; done

polybar -c ~/Software/esta_base/configs/P520_arch/polybar_config.ini dp-bottom &
polybar -c ~/Software/esta_base/configs/P520_arch/polybar_config.ini hdmi-top &
polybar -c ~/Software/esta_base/configs/P520_arch/polybar_config.ini hdmi-bot &
