https://youtu.be/0xuP1GQLPpI
https://mirrors.mit.edu/archlinux/iso/2024.08.01/
    archlinux-2024.08.01-x86_64.iso                    01-Aug-2024 14:38          1182826496



iso etcher: https://youtu.be/0xuP1GQLPpI
https://mirrors.mit.edu/archlinux/iso/2024.08.01/
    /home/ab/Documents/deb/usbimager_1.0.10_uf-x86_64-linux-x11/bin/
    sudo ./usbimager


boot into usb
select arch

arch terminal

iwctl
    station list
    station wlan0 get-networks
    station wlan0 connect 1127APhyAndFriends
    exit

archinstall
    install language English (100%)
    Mirrors: USA
    locales:
        keyboard laylot: us
        locale language: en_US
        local encoding: UTF-8
    disk config:
        use best effort partition layout
        kingston insert image 08/22/24
        ext4
        seperate /home
        insert table image 08/22/24
    disk encriptions: None
    Bootloader: Systemd-boot
    unified kernel image: False
    Swap: True on zram
    root password: disabled
    user profile
        username: esta
        password: newer prefix with old password formula
        superuser yes
    profile:
        type: Xorg
        fraphics drivers: AMD/ATI open source
    audio: pipewire
    kernels: linux, linux-lts
    additional packages: None
    Netowork config: NetworkManager
    Timezone: America/New_York
    Automatic time sync (NTP): True



sudo pacman -Syu
sudo pacman -S neofetch i3 terminator chrmoium dmenu git base-devel github-cli
sudo pacman -S --needed thunar mousepad thunar-archive-plugin thunar-media-tags-plugin
sudo pacman -S --needed lxtask lxappearance-gtk3 materia-gtk-theme papirus-icon-theme	
sudo pacman -S --needed ranger rofi dmenu firefox vlc
sudo pacman -S --needed maim xclip xdotool gnome-keyring picom brightnessctl




https://gist.github.com/fjpalacios/441f2f6d27f25ee238b9bfcb068865db

sudo nano /etc/pacman.conf
    VerbosePkgLists
    Color
    ILoveCandy

https://gist.github.com/fjpalacios/441f2f6d27f25ee238b9bfcb068865db
    sudo pacman -S xorg-server xorg-apps xorg-xinit
    sudo pacman -S noto-fonts ttf-ubuntu-font-family ttf-dejavu ttf-freefont
    sudo pacman -S ttf-liberation ttf-droid ttf-roboto terminus-font
    sudo pacman -S ttf--font-awesome

    sudo pacman -S tlp tlp-rdw powertop acpi
    sudo systemctl enable tlp
    check again: maybe did not start well
        sudo systemctl enable tlp-sleep
        sudo systemctl mask systemd-rfkill.service
        sudo systemctl mask systemd-rfkill.socket

    yay -S slimbookbattery
    yay -S slimbookamdcontroller


configure ~/.xinitrc
    cp /etc/X11/xinit/xinitrc ~/.xinitrc 
    https://github.com/coditva/i3-config/blob/master/xinitrc


https://github.com/Jguer/yay
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -si

github:


yay -S google-chrome
yay -S visual-studio-code-bin

i3 config working on:
    cp ~/.config/i3/config ~/Software/esta_base/configs/Inspiron_16_5625/
    rm -rf ~/.config/i3/config
    ln -s ~/Software/esta_base/configs/Inspiron_16_5625/config ~/.config/i3/config
    cp ~/Software/esta_base/configs/P520/i3blocks.conf ~/Software/esta_base/configs/Inspiron_16_5625/

picom:
    cp /etc/xdg/picom.conf ~/Software/esta_base/configs/Inspiron_16_5625/

work on:
    # compositing:
    #     picom
    brightness: https://www.reddit.com/r/i3wm/comments/pfslli/adjusting_brightnessbacklight_of_the_screen_using/
    volume
    # batter info
    # battery optimisations
        # tlp, slimbookbattery
    hybrid-sleep
    conda
    # xinitrc
    xserver settings
    # wifi
    #     sudo pacman -S --needed network-manager-applet
    # start up programs
    # screen shot