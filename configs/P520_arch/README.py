/home/esta/Software/esta_base/configs/Inspiron_16_5625/README.py
yay ventoy-bin:
    worked
    made 4GB kingston pendrive ventoy

https://mirrors.mit.edu/archlinux/iso/2024.09.01/
    archlinux-2024.09.01-x86_64.iso                    01-Sep-2024 12:41          1168146432

on arch Inspiron_16_5625
    yay ventoy-bin:
    worked
    made 4GB kingston pendrive ventoy

in P520_arch:
    ventoy
    arch
    boot normal mode
    arch install option
    copying rootfs to RAM 


iwctl
    station list
    station wlan0 get-networks
    station wlan0 connect 1127APhyAndFriends
    exit
ping google.com



archinstall
    install language English (100%)
    Mirrors: USA
    locales:
        keyboard laylot: us
        locale language: en_US
        local encoding: UTF-8
    disk config:
        use best effort partition layout
        CT500P3SSD8 (image 092724)
        ext4
        seperate /home
        new partition table (image 092724)
    disk encriptions: None
    Bootloader: Systemd-boot
    unified kernel image: False
    Swap: True on zram
    root password: disabled
    user account
        username: ab
        password: old password
        superuser yes
        user summary (image 092724)
    profile:
        type: Xorg
        graphics drivers: All open-source
    audio: pipewire
    kernels: linux, linux-hardened, linux-lts, linux-zen
    additional packages: None
    Netowork config: NetworkManager
    Timezone: America/New_York
    Automatic time sync (NTP): True

chroor into new installation:
    no
    reboot

sudo pacman -Syu
https://github.com/Jguer/yay
sudo pacman -S --needed  i3 terminator chrmoium dmenu git base-devel github-cli nano
git clone https://aur.archlinux.org/yay-bin.git
cd yay-bin
makepkg -si

xinitrc:
    cp /etc/X11/xinit/xinitrc ~/.xinitrc 
    commented several lines
    exec i3
    from https://github.com/coditva/i3-config/blob/master/xinitrc
    cp ~/Software/esta_base/configs/Inspiron_16_5625/xinitrc ~/Software/esta_base/configs/P520_arch/xinitrc
    rm -rf ~/.xinitrc
    ln -s ~/Software/esta_base/configs/P520_arch/xinitrc ~/.xinitrc


gh auth login
mkdir Software
cd Software
gh repo clone estavrionto/esta_base

yay -S visual-studio-code-bin mousepad google-chrome
yay -S lxtask lxappearance-gtk3 discord discord-screenaudio shotwell pavucontrol
yay -S thunar thunar-archive-plugin thunar-media-tags-plugin gvfs thunar-volman gvfs-mtp xarchiver unzip zip unrar p7zip ntfs-3g
yay -S xorg-xinput acpi xclip xdotool gnome-keyring picom brightnessctl bash-completion neofetch wget
yay -S gimp ffmpegthumbnailer tumbler tumbler-extra-thumbnailers maim nm-connection-editor network-manager-applet


graphics:
yay -S yay vulkan-amdgpu-pro amdgpu-pro-oglp lib32-libdrm lib32-glib2
yay -S mesa lib32-mesa vulkan-radeon lib32-vulkan-radeon libva-mesa-driver libva-utils
You could use "lspci -v" and look at what driver is in use under your VGA controller.
vulkaninfo --summary


# https://gist.github.com/fjpalacios/441f2f6d27f25ee238b9bfcb068865db
yay -S materia-gtk-theme papirus-icon-theme	
yay -S noto-fonts ttf-ubuntu-font-family ttf-dejavu ttf-freefont ttf-liberation ttf-droid ttf-roboto terminus-font ttf-font-awesome adobe-source-code-pro-fonts
list fonts: fc-list|awk '{$1=""}1'|cut -d: -f1|sort|uniq


i3 config working on:
    cp ~/Software/esta_base/configs/Inspiron_16_5625/config ~/Software/esta_base/configs/P520_arch/i3_config
    rm -rf ~/.config/i3/config
    ln -s ~/Software/esta_base/configs/P520_arch/i3_config ~/.config/i3/config
    cp ~/Software/esta_base/configs/Inspiron_16_5625/i3blocks.conf ~/Software/esta_base/configs/P520_arch/i3blocks.conf

configure picom:
    cp ~/Software/esta_base/configs/Inspiron_16_5625/picom.conf ~/Software/esta_base/configs/P520_arch/picom.conf

configure bash
    cp ~/Software/esta_base/configs/Inspiron_16_5625/bashrc ~/Software/esta_base/configs/P520_arch/bashrc
    rm -rf ~/.bashrc
    ln -s ~/Software/esta_base/configs/P520_arch/bashrc ~/.bashrc


terminator:
    cp ~/Software/esta_base/configs/Inspiron_16_5625/terminator_config ~/Software/esta_base/configs/P520_arch/terminator_config
    rm -rf ~/.config/terminator/config
    ln -s ~/Software/esta_base/configs/P520_arch/terminator_config ~/.config/terminator/config

sudo mousepad /etc/pacman.conf
    VerbosePkgLists
    Color
    ILoveCandy

mkdir ~/.config/gtk-4.0/
ln -s ~/.config/gtk-3.0/settings.ini ~/.config/gtk-4.0/settings.ini


showconsolefont
cd /usr/share/kbd/consolefonts
setfont ter-d28b.psf.gz
ter
sudo mousepad /etc/vconsole
    FONT=ter-d28b.psf.gz


mouse: from P520 README
    # flat
    xinput set-prop 9 "libinput Accel Profile Enabled" 0, 1, 0


git config --global user.name "estavrionto"
git config --global user.email estavrionto@gmail.com
# git config pull.rebase false


steam
    https://wiki.archlinux.org/title/Steam
    https://youtu.be/DA5rx7Dw1UI
        sudo mousepad /etc/pacman.conf
            uncomment multilib for 32 bit support

        sudo mousepad /etc/sysctl.d/80-gamecompatibility.conf
            vm.max_map_count = 2147483642


check https://www.reddit.com/r/linux_gaming/comments/18l5itz/mesa_vs_amdvlk_vs_vulkanamdgpupro_drivers/
    suod mousepad /etc/environment
        VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/radeon_icd.i686.json:/usr/share/vulkan/icd.d/radeon_icd.x86_64.json
        AMD_VULKAN_ICD=RADV
        DISABLE_LAYER_AMD_SWITCHABLE_GRAPHICS_1=1


mamba:
    wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
    bash Miniforge3-$(uname)-$(uname -m).sh

    mamba create -n env_jupyter_sep24
    mamba activate env_jupyter_sep24
    mamba install jupyterlab nb_conda_kernels ipywidgets
    # mamba install -c plotly plotly=5.23.0

    mamba create -n env_py_sep24
    mamba activate env_py_sep24
    mamba install ipykernel pandas numpy scipy matplotlib
    mamba install -c plotly plotly=5.23.0
    mamba install ipykernel








