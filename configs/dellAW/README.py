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


# %command%  -vulkan_disable_graphics_pipeline_library -vulkan_disable_steam_shader_cache
# -gl
# +fps_max 60 -high  -map dota -novid -nojoy -novr -vulkan -vulkan_disable_graphics_pipeline_library -vulkan_disable_steam_shader_cache


# git config
# git config --global user.name "estavrionto"
# git config --global user.email estavrionto@gmail.com

# pretty ls with folder sizes
# alias lll='python3 ~/esta_base/scripts/ls_dir_size.py'


# sudo nala install xclip xdotool maim

# installing lutris
# https://software.opensuse.org/download.html?project=home%3Astrycore&package=lutris


# echo 'deb http://download.opensuse.org/repositories/home:/strycore/Debian_Testing/ /' | sudo tee /etc/apt/sources.list.d/home:strycore.list
# curl -fsSL https://download.opensuse.org/repositories/home:strycore/Debian_Testing/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home_strycore.gpg > /dev/null
# sudo apt update
# sudo apt install lutris
# sudo nala install fonts-noto


# 071523
# cd /etc/network
# sudo cat interfaces
# sudo cp ./interfaces ./interfaces.save
# sudo systemctl enable systemd-networkd

# started networkmanager sefvicesu


# 083123
# (base) ab@debian:~/Documents$ nvidia-smi
# Thu Aug 31 07:04:10 2023       
# +-----------------------------------------------------------------------------+
# | NVIDIA-SMI 525.125.06   Driver Version: 525.125.06   CUDA Version: 12.0     |
# |-------------------------------+----------------------+----------------------+
# | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
# | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
# |                               |                      |               MIG M. |
# |===============================+======================+======================|
# |   0  NVIDIA GeForce ...  On   | 00000000:01:00.0  On |                  N/A |
# | N/A   62C    P0    29W /  88W |    909MiB /  6144MiB |      1%      Default |
# |                               |                      |                  N/A |
# +-------------------------------+----------------------+----------------------+
                                                                               
# +-----------------------------------------------------------------------------+
# | Processes:                                                                  |
# |  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
# |        ID   ID                                                   Usage      |
# |=============================================================================|
# |    0   N/A  N/A      1170      G   /usr/lib/xorg/Xorg                504MiB |
# |    0   N/A  N/A      1779      G   ...169271152617974388,262144      156MiB |
# |    0   N/A  N/A      1840      G   ...961179774181519899,262144        7MiB |
# |    0   N/A  N/A      2118      G   ...RendererForSitePerProcess       70MiB |
# |    0   N/A  N/A     28363      G   ...veSuggestionsOnlyOnDemand      165MiB |
# +-----------------------------------------------------------------------------+
# nvidia 535 driver install
# https://www.reddit.com/r/debian/comments/15didi9/comment/ju7pp7u/?utm_source=share&utm_medium=web2x&context=3
# https://www.linuxcapable.com/install-nvidia-drivers-on-debian/

# remove Previous Nvidia Installations
# 	First, use a blanket command to remove any traces of Nvidia installation on your system.
# 	sudo apt autoremove nvidia* --purge
# 	To remove the runfile type of installation, use the following command.
# 	sudo /usr/bin/nvidia-uninstall
# 	Lastly, remove the CUDA toolkit runfile installation using the following command.
# 	sudo /usr/local/cuda-X.Y/bin/cuda-uninstall
# 2nd Method: Install Nvidia Drivers – Nvidia Repository
# 	Determine your Graphics Card
# 		The first step for users with aging NVIDIA Graphics cards is to determine what it is and if it is supported, users with brand new cards can skip this part as there is no doubt they will be supported.
# 		First, find your graphics card module.
# 		lspci | grep -e VGA
# 			01:00.0 VGA compatible controller: NVIDIA Corporation GP106M [GeForce GTX 1060 Mobile] (rev a1)

# 	First, ensure you install the following packages, which may be already installed.
# 		sudo nala install dirmngr ca-certificates software-properties-common apt-transport-https dkms curl -y

# 	Import GPG key for Debian 11 Bullseye (using debian11 as debian12 isnt available):
# 		curl -fSsL https://developer.download.nvidia.com/compute/cuda/repos/debian11/x86_64/3bf863cc.pub | sudo gpg --dearmor | sudo tee /usr/share/keyrings/nvidia-drivers.gpg > /dev/null 2>&1
# 	Import Nvidia Repository for Debian 11 Bullseye:
# 		echo 'deb [signed-by=/usr/share/keyrings/nvidia-drivers.gpg] https://developer.download.nvidia.com/compute/cuda/repos/debian11/x86_64/ /' | sudo tee /etc/apt/sources.list.d/nvidia-drivers.list
# 	Enable the CONTRIB repository. Run this even if you already have it enabled to be safe.
# 		sudo add-apt-repository contrib
# 	Install Nvidia Drivers – Proprietary or Opensource options
# 	Update your sources list to reflect the newly added repository.
# 		sudo apt update
# 	Next, install the latest NVIDIA drivers.
# 	Install NVIDIA Drivers With Cuda Support (Proprietary):
# 		sudo apt install nvidia-driver cuda nvidia-smi nvidia-settings
# last
# 	Reboot your system once done.
# 		sudo reboot
# 	Verify the installation by running NVIDIA-SMI as the manual installation steps showed beforehand.
# 		nvidia-smi
# Install 32-bit Support for Nvidia Drivers
# 	32-bit support can be easily enabled and installed first. Install the 64-bit drivers above, then proceed with the following steps.
# 	First, enable 32-bit architecture.
# 	sudo dpkg --add-architecture i386
# 	Update the APT-CACHE to reflect the changes to the architecture.
# 	sudo apt update
# 	Install 32-bit support, and remove the Cuda package “libcuda1-i386” for those users not requiring it.
# 	sudo apt install libcuda1-i386 nvidia-driver-libs-i386
# 	Reboot your PC.
# 	sudo reboot


used:
	sudo apt autoremove nvidia* --purge
	sudo /usr/bin/nvidia-uninstall
	sudo /usr/local/cuda-X.Y/bin/cuda-uninstall
	lspci | grep -e VGA
	sudo nala install dirmngr ca-certificates software-properties-common apt-transport-https dkms curl -y
	curl -fSsL https://developer.download.nvidia.com/compute/cuda/repos/debian11/x86_64/3bf863cc.pub | sudo gpg --dearmor | sudo tee /usr/share/keyrings/nvidia-drivers.gpg > /dev/null 2>&1
	echo 'deb [signed-by=/usr/share/keyrings/nvidia-drivers.gpg] https://developer.download.nvidia.com/compute/cuda/repos/debian11/x86_64/ /' | sudo tee /etc/apt/sources.list.d/nvidia-drivers.list
	sudo add-apt-repository contrib
