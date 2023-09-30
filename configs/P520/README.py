# debian iso download
# https://mirror.accum.se/cdimage/weekly-builds/amd64/iso-cd/debian-testing-amd64-netinst.iso

# secure boot enabled

# host name: P520
# domain name: 

# no root
# username, password 


# 1GB EFI
# 30GB ext4 /
# 33GB swap
# 435GB ext4 /home
# install debian
    # base system


# sudo apt install nala
# sudo nala install i3 xinit chromium git gh 

# gh auth login 
# gh repo clone ChrisTitusTech/Debian-titus
# gh repo clone estavrionto/esta_base


# https://code.visualstudio.com/docs/setup/linux
    # sudo nala install wget gpg
    # wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
    # sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
    # sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
    # rm -f packages.microsoft.gpg
    # Then update the package cache and install the package using:

    # sudo nala install apt-transport-https
    # sudo nala update
    # sudo nala install code # or code-insiders


# wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# sudo nala install ./google-chrome-stable_current_amd64.deb

# changed trixie to testing in sources
    # deb http://deb.debian.org/debian/ testing main contrib non-free non-free-firmware
    # deb-src http://deb.debian.org/debian/ testing non-free-firmware

    # deb http://security.debian.org/debian-security testing-security main non-free-firmware
    # deb-src http://security.debian.org/debian-security testing-security main non-free-firmware

    # # trixie-updates, to get updates before a point release is made;
    # # see https://www.debian.org/doc/manuals/debian-reference/ch02.en.html#_updates_and_backports
    # deb http://deb.debian.org/debian/ testing-updates main non-free-firmware
    # deb-src http://deb.debian.org/debian/ testing-updates main non-free-firmware

# https://wiki.debian.org/AtiHowTo#Identification
    # sudo nala install firmware-amd-graphics libgl1-mesa-dri libglx-mesa0 mesa-vulkan-drivers xserver-xorg-video-all


    # sudo dpkg --add-architecture i386 && sudo nala update
    # Then, to install the relevant libraries:

    # sudo nala install libglx-mesa0:i386 mesa-vulkan-drivers:i386 libgl1-mesa-dri:i386

    # sudo nala install radeontop

# sudo nala install terminator thunar lxtask lxappearance arandr radeontop network-manager wireplumber pulseaudio pavucontrol xclip xdotool maim i3blocks nitrogen

# mkdir ~/.fonts
# cd ~/.fonts/
# gh repo clone sahibjotsaggu/San-Francisco-Pro-Fonts
# fc-cache -v


# apperarance
    # https://askubuntu.com/questions/598943/how-to-de-uglify-i3-wm
    # sudo nala install gtk-chtheme
    # mkdir ~/.themes
    # cd ~/.themes
    # gh repo clone EliverLara/Nordic
    # sudo nala install fonts-noto

    # alias ll='ls -alh' to .bashrc
    # pretty ls with folder sizes
    # alias lll='python3 ~/esta_base/scripts/ls_dir_size.py'

    # cp ~/esta_base/configs/dellAW/i3blocks.conf ~/esta_base/configs/P520/


    # cp  ~/esta_base/configs/dellAW/config ~/esta_base/configs/P520/

    # rm ~/.config/i3/config
    # ln -s ~/esta_base/configs/P520/config ~/.config/i3/config 

    # lxappearance:
        # nordic theme

    # ~/.bash_profile
    # Use GTK styles for QT apps
    # requires qt5-style-plugins to be installed
    # export QT_STYLE_OVERRIDE="gtk2"
    # export QT_QPA_PLATFORMTHEME="gtk2"

# git config --global user.name "estavrionto"
# git config --global user.email estavrionto@gmail.com

# https://wiki.debian.org/PulseAudio#Solving_Problems
# https://wiki.debian.org/PipeWire#For_PulseAudio
# sudo nala install wireplumber pipewire-pulse
# systemctl --user restart pulseaudio.service
# systemctl --user --now enable wireplumber.service

# discord https://github.com/maltejur/discord-screenaudio:
# sudo nala install -y build-essential cmake qtbase5-dev qtwebengine5-dev libkf5notifications-dev libkf5xmlgui-dev libkf5globalaccel-dev pkg-config libpipewire-0.3-dev git
# git clone https://github.com/maltejur/discord-screenaudio.git
# cd discord-screenaudio
# cmake -B build
# cmake --build build --config Release
# sudo cmake --install build


# sudo nala install steam mangohud

# mamba https://github.com/conda-forge/miniforge
# wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh

