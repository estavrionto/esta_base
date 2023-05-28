# install instructions
# https://askubuntu.com/questions/726972/dual-boot-windows-10-and-linux-ubuntu-on-separate-hard-drives
# 1GB EFI
# 30GB ext4 /
# 20GB swap
# 445GB ext4 /home
# install debian
# sudo apt install i3 xinit chromium git gh nala 
# gh repo clone ChrisTitusTech/Debian-titus
# gh repo clone estavrionto/esta_base
# https://code.visualstudio.com/docs/setup/linux
# wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# sudo nala install ./google-chrome-stable_current_amd64.deb terminator thunar lxtask lxappaearance arandr 




# Debian Bookworm https://wiki.debian.org/NvidiaGraphicsDrivers
# sudo nala install linux-headers-amd64
# sudo nano /etc/apt/sources.list
# deb http://deb.debian.org/debian/ bookworm main contrib non-free non-free-firmware
# sudo nala update
# sudo nala install nvidia-driver firmware-misc-nonfree
		# Notices:
		#   adduser: Warning: The home dir /var/run/nvpd/ you specified can't be accessed: No such file or directory

# sudo reboot
# had to make changes to GRUb to disable opensource frivers by nomodeset and 
	# alseo removed quiet
	# cat /etc/default/grub
	# sudo nano  /etc/default/grub
		# edited quite > nomodeset
	# asudo update-grub

# sudo cp /etc/default/grub /etc/default/grub.bak
# xrandr --output HDMI-0 --mode 1920x1080 --pos 1920x0 --rotate normal --output DP-0 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-1 --off --output DP-2 --off --output DP-1-1 --off --output HDMI-1-1 --off --output HDMI-1-2 --off --output DP-1-2 --off

# mkdir ~/.fonts
# cd ~/.fonts/
# gh repo clone sahibjotsaggu/San-Francisco-Pro-Fonts
# fc-cache -v
# rm ~/.config/i3/config
# ln -s ~/esta_base/configs/dellAW/config ~/.config/i3/config 

# sudo nala install papirus-icon-theme
# steam installation
# https://wiki.debian.org/Steam
# https://wiki.debian.org/NvidiaGraphicsDrivers#multiarch-install
	# sudo dpkg --add-architecture i386
	# sudo nala update
	# sudo nala install nvidia-driver-libs:i386


# sudo nala install pulseaudio
# sudo nala install pavucontrol


# apperarance

# https://askubuntu.com/questions/598943/how-to-de-uglify-i3-wm
# sudo nala install gtk-chtheme

# mkdir ~/.themes
# cd ~/.themes
# gh repo clone EliverLara/Nordic


# search for active gpu: lspci -vnnn | perl -lne 'print if /^\d+\:.+(\[\S+\:\S+\])/' | grep VGA

# sudo nala install network-manager nvtop
# alias ll='ls -alh' to .bashrc
# touch ~/.Xresources
# echo "Xft.dpi: 96" >> ~/.Xresources


# %command% -vulkan -vulkan_disable_graphics_pipeline_library -vulkan_disable_steam_shader_cache