#!/usr/bin/env python3
import subprocess

def sh(Command):
    return subprocess.check_output(Command,shell=True,universal_newlines=True)
import sys
import json

i3_msg = 'i3-msg '

def scratchpad_show(w_class,width,height):
    sh("i3-msg '[class="+w_class+"] scratchpad show, resize set "+width+"px "+height+"px, move position center'")

def get_resolution():
    i3_msg_t = 'i3-msg -t '
    all_commmands = ['run_command', 'get_workspaces', 'get_outputs', 'get_tree', 'get_marks', 'get_bar_config', 'get_binding_modes', 'get_version', 'get_config']

    sh_json_get_ws = sh(i3_msg_t + all_commmands[1])[:-1]

    json_get_ws = json.loads(sh_json_get_ws)
    for i in json_get_ws:
        if i['focused'] == True:
            return i['rect']['width'], i['rect']['height']

width_gap = 40
height_gap = 40
width, height = get_resolution()
if 'Tilda' in sys.argv:
    scratchpad_show('Tilda',str(width-width_gap),str(height-height_gap))

elif 'Rambox' in sys.argv:
    scratchpad_show('Rambox',str(width-width_gap),str(height-height_gap))

elif 'Terminator' in sys.argv:
    scratchpad_show('Terminator',str(width-width_gap),str(height-height_gap))

elif 'Firefox' in sys.argv:
    scratchpad_show('Firefox',str(width-width_gap),str(height-height_gap))

elif 'Chromium-browser' in sys.argv:
    scratchpad_show('Chromium-browser',str(width-width_gap),str(height-height_gap))

print(get_resolution())

