#!/usr/bin/env python3
from esta.general import execute as sh
import sys

def bar(Text):
    print('',Text, end='')

def display(mode):
    location = 'right'
    # function_activation = False
    function_activation = True
    'xrandr --dpi 276 --output eDP-1 --scale 2x2 --output HDMI-1'
    '1,2 = eDP-1, HDMI-1'
    'c,d = connected, disconnected'
    'f,t = false, true'
    # sh_1ct_2d = ['eDP-1 connected primary 1920x1080+0+0 (normal left inverted right x axis y axis) 309mm x 173mm\n']
    sh_1ct_2d = ['eDP-1 connected primary 1920x1080+0+0 (normal left inverted right x axis y axis) 309mm x 174mm\n']

    # sh_1cf_2cf = ['eDP-1 connected primary 1920x1080+0+0 (normal left inverted right x axis y axis) 309mm x 173mm\nHDMI-1 connected (normal left inverted right x axis y axis)\n']
    sh_1cf_2cf = ['eDP-1 connected primary 1920x1080+0+0 (normal left inverted right x axis y axis) 309mm x 174mm\nHDMI-1 connected (normal left inverted right x axis y axis)\n']

    sh_status_gatech_unconfigured_2 = ['eDP-1 connected primary 1920x1080+0+0 (normal left inverted right x axis y axis) 309mm x 174mm\nDVI-I-2-2 connected 1080x1920+1920+0 right (normal left inverted right x axis y axis) 527mm x 296mm\nDVI-I-1-1 connected 1920x1080+0+344 (normal left inverted right x axis y axis) 527mm x 296mm\n']
    sh_status_gatech_unconfigured_1 = ['eDP-1 connected primary 1920x1080+0+0 (normal left inverted right x axis y axis) 309mm x 174mm\nDVI-I-2-2 connected (normal left inverted right x axis y axis)\nDVI-I-1-1 connected (normal left inverted right x axis y axis)\n']
    sh_status_gatech_configured_1 = ['eDP-1 connected primary 1920x1080+0+1424 (normal left inverted right x axis y axis) 309mm x 174mm\nDVI-I-2-2 connected 1080x1920+1920+0 right (normal left inverted right x axis y axis) 527mm x 296mm\nDVI-I-1-1 connected 1920x1080+0+344 (normal left inverted right x axis y axis) 527mm x 296mm\n']
    sh_status_gatech_configured_2 = ['eDP-1 connected primary 1920x1080+0+1424 (normal left inverted right x axis y axis) 309mm x 174mm\nDVI-I-2-2 connected 1920x1080+0+344 (normal left inverted right x axis y axis) 527mm x 296mm\nDVI-I-1-1 connected 1080x1920+1920+0 right (normal left inverted right x axis y axis) 527mm x 296mm\n']
    cm_status = 'xrandr|grep connected|grep -v disconnected'
    cm_1cf_2d_1ct_2d   = 'xrandr --output HDMI-1 --off --output DVI-I-2-2 --off --output DVI-I-1-1 --off && nitrogen --restore'

    if location == 'top':
        'outputs for HDMI-1 top of eDP-1'
        sh_1ct_2ct = ['eDP-1 connected primary 1920x1080+0+1080 (normal left inverted right x axis y axis) 309mm x 174mm\nHDMI-1 connected 1920x1080+0+0 (normal left inverted right x axis y axis) 160mm x 90mm\n']
        sh_1cf_2d = ['eDP-1 connected primary 1920x1080+0+1080 (normal left inverted right x axis y axis) 309mm x 174mm\n']

        'commands for HDMI-1 top of eDP-1'
        cm_1cf_2cf_1ct_2ct = 'xrandr --output HDMI-1 --auto --pos 0x0 --output eDP-1 --primary --mode 1920x1080 --pos 0x1080 && nitrogen --restore'

    if location == 'left':
        'outputs for HDMI-1 left of eDP-1'
        sh_1ct_2ct = ['eDP-1 connected primary 1920x1080+1920+0 (normal left inverted right x axis y axis) 309mm x 174mm\nHDMI-1 connected 1920x1080+0+0 (normal left inverted right x axis y axis) 160mm x 90mm\n']
        sh_1cf_2d = ['eDP-1 connected primary 1920x1080+0+0 (normal left inverted right x axis y axis) 309mm x 174mm\n']

        'commands for HDMI-1 left of eDP-1'
        cm_1cf_2cf_1ct_2ct = 'xrandr --output HDMI-1 --auto --pos 0x0 --output eDP-1 --primary --mode 1920x1080 --pos 1920x0 && nitrogen --restore'

    if location == 'right':
        'outputs for HDMI-1 right of eDP-1'
        sh_1ct_2ct = ['eDP-1 connected primary 1920x1080+0+0 (normal left inverted right x axis y axis) 309mm x 174mm\nHDMI-1 connected 1920x1080+1920+0 (normal left inverted right x axis y axis) 160mm x 90mm\n']
        sh_1cf_2d = ['eDP-1 connected primary 1920x1080+0+0 (normal left inverted right x axis y axis) 309mm x 174mm\n']

        'commands for HDMI-1 right of eDP-1'
        cm_1cf_2cf_1ct_2ct = 'xrandr --output HDMI-1 --auto --pos 1920x0 --output eDP-1 --primary --mode 1920x1080 --pos 0x0 && nitrogen --restore'


    cm_gatech_activate_displays = 'xrandr --output DVI-I-1-1 --mode 1920x1080 --pos 0x344 --rotate normal --output eDP-1 --primary --mode 1920x1080 --pos 0x1424 --rotate normal --output DVI-I-2-2 --mode 1920x1080 --pos 1920x0 --rotate right'
    cm_gatech_activate_displays = 'xrandr --output DVI-I-2-2 --mode 1920x1080 --pos 0x344 --rotate normal --output eDP-1 --primary --mode 1920x1080 --pos 0x1424 --rotate normal --output DVI-I-1-1 --mode 1920x1080 --pos 1920x0 --rotate right'


    sh_status = [sh(cm_status)]
    # print(sh_status)
    sy_t = ''
    sy_f = ''
    sy_tt = ''
    sy_foreign = ''
    sy_t = 'eDP-1'
    sy_f = 'f'
    sy_tt = 'tt'
    sy_foreign = 'ff'
    sy_gatech_uncon = 'GT*'
    sy_gatech_con = 'GT'


    if mode == 'normal' and function_activation:
        if sh_status == sh_1ct_2d:
            "normal conditions without hdmi, do nothing"
            bar(sy_t)
            sh(cm_1cf_2d_1ct_2d)
            # print('ctd')
        elif sh_status == sh_1cf_2cf:
            'hdmi connected, configure hdmi'
            # print('here 1')
            bar(sy_t+sy_f)
            sh(cm_1cf_2cf_1ct_2ct)
            # print('cfcf')
        elif sh_status == sh_1ct_2ct:
            'hdmi already configured, do nothing'
            bar(sy_tt)
            # print('ctct')
            # pass
        elif sh_status == sh_1cf_2d:
            'hdmi removed, reconfigure edp'
            bar(sy_f)
            sh(cm_1cf_2d_1ct_2d)
            # print('cfd')
        elif sh_status in [sh_status_gatech_unconfigured_2,sh_status_gatech_unconfigured_1]:
            bar(sy_gatech_uncon)
            sh(cm_gatech_activate_displays)
        elif sh_status in [sh_status_gatech_configured_1,sh_status_gatech_configured_2]:
            bar(sy_gatech_con)
        else:
            'foreign layout'
            # print('here 2')
            print('foreign detected')
            bar(sy_foreign)
            sh(cm_1cf_2cf_1ct_2ct)
    elif mode == 'status':
        print(sh_status)
    # print(sh_status,mode)


def mouse(mode = 'normal'):
    cm_hp_id = "xinput | grep 'E-Signal/A-One USB Gaming Mouse  '"
    
    
    sh_map_1 = '1 2 3 4 5 6 11 12 13 \n'
    sh_map_2 = '1 2 3 4 5 6 11 8 9 \n'
    try:
        sh_hp_id = [i[3:5] for i in sh(cm_hp_id).split('\t') if i[:3] == 'id='][0]

        cm_set_map_1 = 'xinput set-button-map '+sh_hp_id+' 1 2 3 4 5 6 11 12 13 10 11 12 13 14 15 16 17 18 19 20'
        cm_set_map_2 = 'xinput set-button-map '+sh_hp_id+' 1 2 3 4 5 6 11 8 9 10 11 12 13 14 15 16 17 18 19 20'

        cm_check_conf = 'xinput get-button-map '+sh_hp_id

        cm_ms_acc_check = "xinput list-props "+sh_hp_id+" 2>/dev/null | fgrep 'libinput Accel Profile Enabled ('"
        cm_ms_acc_zero = "xinput --set-prop "+sh_hp_id+" 'libinput Accel Profile Enabled' 0, 1"
        if sh(cm_check_conf) not in [sh_map_1, sh_map_2]:
            cm_set_map_1 = 'xinput set-button-map '+sh_hp_id+' 1 2 3 4 5 6 11 12 13 10 11 12 13 14 15 16 17 18 19 20'
            cm_set_map_2 = 'xinput set-button-map '+sh_hp_id+' 1 2 3 4 5 6 11 8 9 10 11 12 13 14 15 16 17 18 19 20'
            sh(cm_set_map_1)
            sh(cm_ms_acc_zero)
            bar('map set')
        elif sh(cm_check_conf) == sh_map_1 and sh(cm_ms_acc_check)[-5:] == "0, 1\n":
            bar('🖱️')
        elif sh(cm_check_conf) == sh_map_2 and sh(cm_ms_acc_check)[-5:] == "0, 1\n":
            bar('🖲️')
    except:
        # prints box for touch pad only being used
        bar('') 

def battery(mode = 'normal'):
    cm_status     = 'cat /sys/class/power_supply/BAT0/status'
    cm_capacity   = 'cat /sys/class/power_supply/BAT0/capacity'
    cm_xkb_layout = 'KeyboardLayout.py c-e'
    cm_lock       = 'i3lock -t -i ~/myHDD/Works/Arvind_art_face/lock12.png'
    cm_sleep      = 'sleep 1'
    cm_suspend      = 'systemctl hybrid-sleep'

    sh_status     = 'Discharging\n'


    if sh(cm_status) == sh_status:
        if int(sh(cm_capacity)[:-1]) >= 7:
            
            sh(cm_xkb_layout)
            print('next')
            sh(cm_lock)
            print('next')
            sh(cm_sleep)
            print('next')
            sh(cm_suspend)
            print('next')


def sound(mode):
    print('sound')
def always():
    display('normal')
    mouse()
    # print('display-sound')
    # pass



# print('start')
if len(sys.argv) == 3:
    # print(len(sys.argv))
    arguments_1 = {
        'display': display,
        'mouse'  : mouse,
        'sound'  : sound,
        'battery': battery
        }
    if sys.argv[1] in arguments_1.keys():
        # print('aa')
        arguments_1[sys.argv[1]](sys.argv[2])
else:
    # print('else',len(sys.argv))
    always()

# print('end')

# command_xrandr = 'xrandr'

# output_xrandr = es.execute(command_xrandr)

# for j,i in output_xrandr:
#     print(i)