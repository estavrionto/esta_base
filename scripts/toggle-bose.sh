#!/bin/bash

DEVICE="4C:87:5D:9F:E2:E9"
STATUS=$(bluetoothctl info "$DEVICE" | grep "Connected: yes")

if [ -n "$STATUS" ]; then
    bluetoothctl disconnect "$DEVICE"
    notify-send "Bose NC 700 Disconnected"
else
    bluetoothctl connect "$DEVICE"
    notify-send "Bose NC 700 Connected"
fi
