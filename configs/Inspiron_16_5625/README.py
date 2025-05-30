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
sudo pacman -S --needed neofetch i3 terminator chrmoium dmenu git base-devel github-cli


sudo pacman -S --needed thunar mousepad thunar-archive-plugin thunar-media-tags-plugin gvfs thunar-volman gvfs-mtp 
sudo pacman -S --needed lxtask lxappearance-gtk3 materia-gtk-theme papirus-icon-theme	
sudo pacman -S --needed maim xclip xdotool gnome-keyring picom brightnessctl
yay -S discord bash-completion discord-screenaudio xarchiver
sudo pacman -S --needed unzip zip unrar p7zip 
yay gimp ffmpegthumbnailer tumbler tumbler-extra-thumbnailers shotwell



https://gist.github.com/fjpalacios/441f2f6d27f25ee238b9bfcb068865db

sudo nano /etc/pacman.conf
    VerbosePkgLists
    Color
    ILoveCandy


terminator:
    cp ~/.config/terminator/config ~/Software/esta_base/configs/Inspiron_16_5625/terminator_config
    rm -rf ~/.config/terminator/config
    ln -s ~/Software/esta_base/configs/Inspiron_16_5625/terminator_config ~/.config/terminator/config

configure ~/.xinitrc
    cp /etc/X11/xinit/xinitrc ~/.xinitrc 
    https://github.com/coditva/i3-config/blob/master/xinitrc
    cp ~/.xinitrc ~/Software/esta_base/configs/Inspiron_16_5625/xinitrc
    rm -rf ~/.xinitrc
    ln -s ~/Software/esta_base/configs/Inspiron_16_5625/xinitrc ~/.xinitrc
configure bash
    cp ~/.bashrc ~/Software/esta_base/configs/Inspiron_16_5625/bashrc
    rm -rf ~/.bashrc
    ln -s ~/Software/esta_base/configs/Inspiron_16_5625/bashrc ~/.bashrc

configure gtk2:
    cp ~/.gtkrc-2.0 ~/Software/esta_base/configs/Inspiron_16_5625/gtkrc_2
    rm -rf ~/.gtkrc-2.0
    ln -s ~/Software/esta_base/configs/Inspiron_16_5625/gtkrc_2 ~/.gtkrc-2.0.mine
mkdir ~/.config/gtk-4.0/
ln -s ~/.config/gtk-3.0/settings.ini ~/.config/gtk-4.0/settings.ini


https://gist.github.com/fjpalacios/441f2f6d27f25ee238b9bfcb068865db
    sudo pacman -S xorg-server xorg-apps xorg-xinit
    sudo pacman -S noto-fonts ttf-ubuntu-font-family ttf-dejavu ttf-freefont
    sudo pacman -S ttf-liberation ttf-droid ttf-roboto terminus-font
    sudo pacman -S --needed ttf-font-awesome adobe-source-code-pro-fonts


    list fonts: fc-list|awk '{$1=""}1'|cut -d: -f1|sort|uniq
    sudo pacman -S tlp tlp-rdw powertop acpi
    sudo systemctl enable tlp
    check again: maybe did not start well
        sudo systemctl enable tlp-sleep
        sudo systemctl mask systemd-rfkill.service
        sudo systemctl mask systemd-rfkill.socket

    yay -S slimbookbattery acpi
    yay -S slimbookamdcontroller



xdg-desktop-portal xapp

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


mamba:

    mamba activate env_jupyter_aug24
    mamba install jupyterlab nb_conda_kernels ipywidgets
    mamba install -c plotly plotly=5.23.0

    mamba activate env_py_aug24
    mamba install -c plotly plotly=5.23.0
    mamba install ipykernel

    


    ln -s ~/BackUp/education/GaTech/Research/fanLab ~/Research/fanLab



work on:
    # wifi
    #     sudo pacman -S --needed network-manager-applet
    # start up programs
    # screen shot
    # discord
    # brightness: https://www.reddit.com/r/i3wm/comments/pfslli/adjusting_brightnessbacklight_of_the_screen_using/
    # volume:
    #     $ xev | awk -F'[ )]+' '/^KeyPress/ { a[NR+2] } NR in a { printf "%-3s %s\n", $5, $8 }'
    # conda, mamba

    dropbox
    tqdm for loop python

    battery optimisations
        acpi, optimisations, battery info
        # tlp, slimbookbattery
    hybrid-sleep
        hibernate needs work on
        # suspend works
    xinitrc
    xserver settings
    microphone
    compositing:
        picom optimisatoin


wifi: https://gatech.service-now.com/technology?id=kb_article_view&sysparm_article=KB0026877

showconsolefont
cd /usr/share/kbd/consolefonts
setfont ter-d28b.psf.gz
ter
sudo vim /etc/vconsole
    FONT=ter-d28b.psf.gz


installed zen kernel
cd /boot/loader/entries
added:
    2024-09-23_linux-zen.conf
        # created from: /boot/loader/entries/2024-08-22_16-37-00_linux-lts.conf
        # Created by: esta
        # Created on: 2024-09-23
        title   Arch Linux (linux-zen)
        linux   /vmlinuz-linux-zen
        initrd  /initramfs-linux-zen.img
        options root=PARTUUID=ffc44a7a-050b-4f84-a185-ea39622f6762 zswap.enabled=0 rw rootfstype=ext4

    2024-09-23_linux-zen-fallback.conf

pavucontrol dark mode:
    https://youtu.be/mOXd_SOrDbA


yay ventoy (-bin is already compiled binaries)
    ran for long time, interrupted
    added 2GB to /root
yay ventoy-bin:
    worked
    made 4GB kingston pendrive ventoy

yay globalprotect
    globalprotect-openconnect-git
        sudo -E gpclient connect --browser chrome vpn.gatech.edu
        sudo gpclient connect vpn.gatech.edu
        gpauth vpn.gatech.edu --browser chrome

    https://live.paloaltonetworks.com/t5/globalprotect-discussions/globalprotect-for-arch-linux/td-p/573976
    cd /home/esta/Software/VPN/GlobalProtect_tar-6.2.0.1-265
    sudo ./install.sh
    globalprotect connect -p vpn.gatech.edu

yay ferdium

fsck:
    from live ventoy arch usb
    https://www.reddit.com/r/linuxquestions/comments/ry2mdp/ext4_optimisation/
    fsck -CMf /dev/nvme0n1p3


got the error:
    https://wiki.archlinux.org/title/Pacman#%22Failed_to_commit_transaction_(conflicting_files)%22_error
    error: could not prepare transaction
    error: failed to commit transaction (conflicting files)
    package: /path/to/file exists in filesystem
    Errors occurred, no packages were upgraded.

    did:
        # sudo pacman -R ferdium-bin
        # sudo pacman -R picom
        # sudo pacman -R firefox
        # sudo pacman -R electron32
        # sudo pacman -R discord
        # sudo pacman -R onlyoffice-bin

        then worked:
            yay 

yay pacman-contrib
paccache -u -r -k0
yay discord
yay firefox
yay onlyoffice-bin
yay ferdium-bin
yay picom


# steam
yay -S mesa lib32-mesa vulkan-radeon lib32-vulkan-radeon libva-mesa-driver libva-utils
yay -S vulkan-radeon lib32-vulkan-radeon libva-mesa-driver libva-utils




