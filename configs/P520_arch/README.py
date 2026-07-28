# /home/esta/Software/esta_base/configs/Inspiron_16_5625/README.py
# yay ventoy-bin:
#     worked
#     made 4GB kingston pendrive ventoy

# https://mirrors.mit.edu/archlinux/iso/2024.09.01/
#     archlinux-2024.09.01-x86_64.iso                    01-Sep-2024 12:41          1168146432

# on arch Inspiron_16_5625
#     yay ventoy-bin:
#     worked
#     made 4GB kingston pendrive ventoy

# in P520_arch:
#     ventoy
#     arch
#     boot normal mode
#     arch install option
#     copying rootfs to RAM 


# iwctl
#     station list
#     station wlan0 get-networks
#     station wlan0 connect 1127APhyAndFriends
#     exit
# ping google.com



# archinstall
#     install language English (100%)
#     Mirrors: USA
#     locales:
#         keyboard laylot: us
#         locale language: en_US
#         local encoding: UTF-8
#     disk config:
#         use best effort partition layout
#         CT500P3SSD8 (image 092724)
#         ext4
#         seperate /home
#         new partition table (image 092724)
#     disk encriptions: None
#     Bootloader: Systemd-boot
#     unified kernel image: False
#     Swap: True on zram
#     root password: disabled
#     user account
#         username: ab
#         password: old password
#         superuser yes
#         user summary (image 092724)
#     profile:
#         type: Xorg
#         graphics drivers: All open-source
#     audio: pipewire
#     kernels: linux, linux-hardened, linux-lts, linux-zen
#     additional packages: None
#     Netowork config: NetworkManager
#     Timezone: America/New_York
#     Automatic time sync (NTP): True

# chroor into new installation:
#     no
#     reboot

# sudo pacman -Syu
# https://github.com/Jguer/yay
# sudo pacman -S --needed  i3 terminator chrmoium dmenu git base-devel github-cli nano
# git clone https://aur.archlinux.org/yay-bin.git
# cd yay-bin
# makepkg -si

# xinitrc:
#     cp /etc/X11/xinit/xinitrc ~/.xinitrc 
#     commented several lines
#     exec i3
#     from https://github.com/coditva/i3-config/blob/master/xinitrc
#     cp ~/Software/esta_base/configs/Inspiron_16_5625/xinitrc ~/Software/esta_base/configs/P520_arch/xinitrc
#     rm -rf ~/.xinitrc
#     ln -s ~/Software/esta_base/configs/P520_arch/xinitrc ~/.xinitrc


# gh auth login
# mkdir Software
# cd Software
# gh repo clone estavrionto/esta_base

# yay -S visual-studio-code-bin mousepad google-chrome
# yay -S lxtask lxappearance-gtk3 discord discord-screenaudio shotwell pavucontrol
# yay -S thunar thunar-archive-plugin thunar-media-tags-plugin gvfs thunar-volman gvfs-mtp xarchiver unzip zip unrar p7zip ntfs-3g
# yay -S xorg-xinput acpi xclip xdotool gnome-keyring picom brightnessctl bash-completion neofetch wget
# yay -S gimp ffmpegthumbnailer tumbler tumbler-extra-thumbnailers maim nm-connection-editor network-manager-applet


# graphics:
# yay -S yay vulkan-amdgpu-pro amdgpu-pro-oglp lib32-libdrm lib32-glib2
# yay -S mesa lib32-mesa vulkan-radeon lib32-vulkan-radeon libva-mesa-driver libva-utils
# You could use "lspci -v" and look at what driver is in use under your VGA controller.
# vulkaninfo --summary


# # https://gist.github.com/fjpalacios/441f2f6d27f25ee238b9bfcb068865db
# yay -S materia-gtk-theme papirus-icon-theme	
# yay -S noto-fonts ttf-ubuntu-font-family ttf-dejavu ttf-freefont ttf-liberation ttf-droid ttf-roboto terminus-font ttf-font-awesome adobe-source-code-pro-fonts
# list fonts: fc-list|awk '{$1=""}1'|cut -d: -f1|sort|uniq


# i3 config working on:
#     cp ~/Software/esta_base/configs/Inspiron_16_5625/config ~/Software/esta_base/configs/P520_arch/i3_config
#     rm -rf ~/.config/i3/config
#     ln -s ~/Software/esta_base/configs/P520_arch/i3_config ~/.config/i3/config
#     cp ~/Software/esta_base/configs/Inspiron_16_5625/i3blocks.conf ~/Software/esta_base/configs/P520_arch/i3blocks.conf

# configure picom:
#     cp ~/Software/esta_base/configs/Inspiron_16_5625/picom.conf ~/Software/esta_base/configs/P520_arch/picom.conf

# configure bash
#     cp ~/Software/esta_base/configs/Inspiron_16_5625/bashrc ~/Software/esta_base/configs/P520_arch/bashrc
#     rm -rf ~/.bashrc
#     ln -s ~/Software/esta_base/configs/P520_arch/bashrc ~/.bashrc


# terminator:
#     cp ~/Software/esta_base/configs/Inspiron_16_5625/terminator_config ~/Software/esta_base/configs/P520_arch/terminator_config
#     rm -rf ~/.config/terminator/config
#     ln -s ~/Software/esta_base/configs/P520_arch/terminator_config ~/.config/terminator/config

# sudo mousepad /etc/pacman.conf
#     VerbosePkgLists
#     Color
#     ILoveCandy

# mkdir ~/.config/gtk-4.0/
# ln -s ~/.config/gtk-3.0/settings.ini ~/.config/gtk-4.0/settings.ini


# showconsolefont
# cd /usr/share/kbd/consolefonts
# setfont ter-d28b.psf.gz
# ter
# sudo mousepad /etc/vconsole
#     FONT=ter-d28b.psf.gz


# mouse: from P520 README
#     # flat
#     xinput set-prop 9 "libinput Accel Profile Enabled" 0, 1, 0


# git config --global user.name "estavrionto"
# git config --global user.email estavrionto@gmail.com
# # git config pull.rebase false


# steam
#     https://wiki.archlinux.org/title/Steam
#     https://youtu.be/DA5rx7Dw1UI
#         sudo mousepad /etc/pacman.conf
#             uncomment multilib for 32 bit support

#         sudo mousepad /etc/sysctl.d/80-gamecompatibility.conf
#             vm.max_map_count = 2147483642


# check https://www.reddit.com/r/linux_gaming/comments/18l5itz/mesa_vs_amdvlk_vs_vulkanamdgpupro_drivers/
#     suod mousepad /etc/environment
#         VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/radeon_icd.i686.json:/usr/share/vulkan/icd.d/radeon_icd.x86_64.json
#         AMD_VULKAN_ICD=RADV
#         DISABLE_LAYER_AMD_SWITCHABLE_GRAPHICS_1=1


# mamba:
#     wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
#     bash Miniforge3-$(uname)-$(uname -m).sh

#     mamba create -n env_jupyter_sep24
#     mamba activate env_jupyter_sep24
#     mamba install jupyterlab nb_conda_kernels ipywidgets
#     # mamba install -c plotly plotly=5.23.0

#     mamba create -n env_py_sep24
#     mamba activate env_py_sep24
#     mamba install ipykernel pandas numpy scipy matplotlib
#     mamba install -c plotly plotly=5.23.0
#     mamba install ipykernel

# moved to i5 System

# # (base) [ab@archlinux ~]$ neofetch
# #                    -`                    ab@archlinux 
# #                   .o+`                   ------------ 
# #                  `ooo/                   OS: Arch Linux x86_64 
# #                 `+oooo:                  Host: B760I GAMING Ver: 1.00 
# #                `+oooooo:                 Kernel: 6.17.9-zen1-1-zen 
# #                -+oooooo+:                Uptime: 17 hours, 5 mins 
# #              `/:-:++oooo+:               Packages: 945 (pacman) 
# #             `/++++/+++++++:              Shell: bash 5.3.9 
# #            `/++++++++++++++:             Resolution: 1920x1080, 1080x1920 
# #           `/+++ooooooooooooo/`           WM: i3 
# #          ./ooosssso++osssssso+`          Theme: Materia-dark-compact [GTK2/3] 
# #         .oossssso-````/ossssss+`         Icons: breeze-dark [GTK2/3] 
# #        -osssssso.      :ssssssso.        Terminal: terminator 
# #       :osssssss/        osssso+++.       CPU: 12th Gen Intel i5-12600K (16) @ 4.900GHz 
# #      /ossssssss/        +ssssooo/-       GPU: AMD ATI Radeon RX 5600 OEM/5600 XT / 5700/5700 XT 
# #    `/ossssso+/:-        -:/+osssso+-     Memory: 9919MiB / 15749MiB 
# #   `+sso+:-`                 `.-/+oso:
# #  `++:.                           `-/+/                           
# #  .`                                 `/                           


# # (base) [ab@archlinux ~]$ 


#     added gpu 5700xt
#     added crucial ssd
#     had to arch usb Boot
#     arch-chroot and create new entry for linux boot manager


#     instealled corectrl fro fan control https://gitlab.com/corectrl/corectrl/-/wikis/Setup

# dota 2
# gamemoderun mangohud  %command% -novid -nojoy -vulkan -high -fullscreen -sdl_displayindex 1 +fps_max 140 -console -map dota -sdlaudiodriver pulse

# gamemoderun mangohud  %command% -novid -nojoy -vulkan -high -fullscreen -sdl_displayindex 1 +fps_max 140 -console -map dota -sdlaudiodriver pulse

# gamemoderun mangohud  %command% -novid -nojoy -sdl_displayindex 1 +fps_max 140 -console

# installed corectrl
# added arctic p14 pro 140mm case fan to front, bot 2 crewerd with case crews, top 1 wire secured

# added fan curve to the bios in chipset, smart fan control

# code /home/ab/Software/esta_base/scripts/i3_per_output_alt_tab.py
# chmod +x /home/ab/Software/esta_base/scripts/i3_per_output_alt_tab.py
# bindsym $alt+Tab exec --no-startup-id /home/ab/Software/esta_base/scripts/i3_per_output_alt_tab.py alt-tab


# pgrep -af i3_per_output_alt_tab.py

# code /home/ab/Software/esta_base/configs/P520_arch/i3-per-output-alt-tab.service

# ln -sf /home/ab/Software/esta_base/configs/P520_arch/i3-per-output-alt-tab.service ~/.config/systemd/user/i3-per-output-alt-tab.service

# systemctl --user daemon-reload


# 122925 Per-output Alt+Tab in i3 (Arch Linux)
# Implemented true per-monitor Alt+Tab by writing a Python helper that listens to workspace focus events via i3-msg -t subscribe and tracks last workspace per output. Switched from in-memory state to file-backed state (/tmp/i3_per_output_ws_history.json) so keybinding invocations can share history. Added verbose logging for debugging. Deployed the listener as a systemd user service with Restart=always to survive i3 reloads and IPC disconnects.

# Key files / locations
# Python helper: /home/ab/Software/esta_base/scripts/i3_per_output_alt_tab.py
# State file: /tmp/i3_per_output_ws_history.json
# Debug log: /tmp/i3_per_output_alt_tab.log
# systemd user service (repo-tracked): /home/ab/Software/esta_base/configs/P520_arch/i3-per-output-alt-tab.service
# systemd symlink: ~/.config/systemd/user/i3-per-output-alt-tab.service
# i3 config binding: bindsym $alt+Tab exec --no-startup-id /home/ab/Software/esta_base/scripts/i3_per_output_alt_tab.py alt-tab

# Important commands (debug / control)
# Start listener manually: i3_per_output_alt_tab.py
# Trigger Alt+Tab manually: i3_per_output_alt_tab.py alt-tab
# Check running instances: pgrep -af i3_per_output_alt_tab.py
# Kill stray instances: pkill -f i3_per_output_alt_tab.py
# Service status: systemctl --user status i3-per-output-alt-tab.service
# Restart service: systemctl --user restart i3-per-output-alt-tab.service
# Live logs (systemd): journalctl --user -u i3-per-output-alt-tab.service -f


# Thermal / stress test cheat-sheet

# CPU stress (worst case AVX)
    # stress-ng --matrix -1 --timeout 10m --metrics-brief
# CPU power / clocks / temps (minimal turbostat)
    # sudo turbostat --interval 1 --Summary --quiet --show Busy%,Avg_MHz,PkgWatt,CoreTmp,PkgTmp
# Set CPU governor (temporary)
    # sudo cpupower frequency-set -g performance
    # # revert
    # sudo cpupower frequency-set -g powersave
# GPU stress (moderate, realistic)
    # gputest /test=pixmark_piano /width=1920 /height=1080 /fullscreen
# GPU stress (heavy, thermal limit)
    # gputest /test=gi /width=1920 /height=1080 /fullscreen
# GPU fan manual test (amdgpu only)
    # echo 1 | sudo tee /sys/class/hwmon/hwmon2/pwm1_enable
    # echo 128 | sudo tee /sys/class/hwmon/hwmon2/pwm1
# revert to auto
    # echo 2 | sudo tee /sys/class/hwmon/hwmon2/pwm1_enable
# Live temps / fans
    # watch -n1 sensors
    # nvtop


# Expected targets
# CPU: ~170 W, <90 C plateau
# GPU junction: <100 C (after airflow + power limit)

# 122925: testing after adding both arctic p14 one blowing on cpu, other on gpu 
# (base) [ab@archlinux ~]$ stress-ng --matrix -1 --timeout 10m --metrics-brief
# stress-ng: info:  [22291] setting to a 10 mins run per stressor
# stress-ng: info:  [22291] dispatching hogs: 16 matrix
# ^Cstress-ng: info:  [22291] stopping 16 stressors
# stress-ng: metrc: [22291] stressor       bogo ops real time  usr time  sys time   bogo ops/s     bogo ops/s
# stress-ng: metrc: [22291]                           (secs)    (secs)    (secs)   (real time) (usr+sys time)
# stress-ng: metrc: [22291] matrix         21221066    343.83   5261.43      6.95     61720.12        4028.01
# stress-ng: info:  [22291] skipped: 0
# stress-ng: info:  [22291] passed: 16: matrix (16)
# stress-ng: info:  [22291] failed: 0
# stress-ng: info:  [22291] metrics untrustworthy: 0
# stress-ng: info:  [22291] successful run completed in 5 mins, 43.83 secs
# (base) [ab@archlinux ~]$ gputest /test=gi /width=1920 /height=1080 /fullscreen

# stress-ng --matrix -1 --timeout 10m --metrics-brief

# 210w gpu, temp at 68, junction at 105
# 170w cpu, temp at 80 to 86


# xinput set-prop "Logitech G502 HERO Gaming Mouse" "libinput Accel Profile Enabled" 0 1 0

# xinput list-props "Logitech G502 HERO Gaming Mouse" |grep Accel



# # mkdir -p ~/.config/polybar
# installed polybar

# code ~/Software/esta_base/configs/P520_arch/polybar_config.ini
# code ~/Software/esta_base/configs/P520_arch/polybar_launch.sh
# chmod +x ~/Software/esta_base/configs/P520_arch/polybar_launch.sh
# exec_always --no-startup-id ~/Software/esta_base/configs/P520_arch/polybar_launch.sh


# 123125 Polybar migration summary 

# Files modified / created

# ~/Software/esta_base/configs/P520_arch/polybar_config.ini
#     Replaced i3bar/i3blocks
#     Global colors copied from old i3 config
#     Bars defined:
#         bar/dp-bottom (DisplayPort-2, bottom)
#         bar/hdmi-top (HDMI-A-0, top)
#         bar/hdmi-bot (HDMI-A-0, bottom, tray enabled)
#     Font set to Source Code Pro:size=13
#     Tray enabled only on hdmi-bot
#     Padding via padding-left/right

# ~/Software/esta_base/configs/P520_arch/polybar_launch.sh
#     Kills existing Polybar
#     Launches hdmi-top, hdmi-bot, dp-bottom

# ~/Software/esta_base/configs/P520_arch/i3_config
#     Removed all bar {} blocks
#     Added exec_always --no-startup-id polybar_launch.sh

# Modules
#     internal/i3
#         pin-workspaces = true, index-sort = true
#         Spacing via label-*-padding = 0
#         Visual separation via label-separator = "|"
#     Time modules (custom/script)
#         time-dual: local + India (1s interval)
#         time-mono: local only
#     Temp module
#         chip-temp runs ~/Software/esta_base/configs/chip-temp.py

# Final layout
#     DP-2 bottom: workspaces + dual time
#     HDMI top: chip temp
#     HDMI bottom: workspaces + time + tray


added ram analysis in jupyter:
    http://localhost:8888/lab/workspaces/auto-7/tree/Software/esta_base/code/RAM_analysis.ipynb

added i3 chortcuts juputer notebook
    http://localhost:8888/lab/workspaces/auto-7/tree/Software/esta_base/scripts/i3_config.ipynb


gamemoderun mangohud  %command% -novid -nojoy -sdl_displayindex 1 +fps_max 140 -console -sdlaudiodriver pulse

You had a global Vulkan override set in /etc/environment.

It forced Vulkan to load old, non-existent ICD files:

radeon_icd.i686.json
radeon_icd.x86_64.json

Modern Arch uses:

radeon_icd.json

Because of the override, Vulkan could not find a driver, so Dota started but never created a window.

Removing those environment variables fixed Vulkan and restored normal game launching.