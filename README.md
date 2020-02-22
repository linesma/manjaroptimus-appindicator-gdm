<img src="https://github.com/linesma/manjaroptimus-appindicator/blob/master/Logo/manjaroptimus-logo02b.png" align="left" width="256" />

# Manjaro-Optimus Indicator GDM
## Indicator and GUI switch for Optimus-Switch on Manjaro that works with Gnome running Wayland.
</br>



![Manjaro-Optimus Indicator](https://github.com/linesma/manjaroptimus-appindicator/blob/master/screenshots/Flow3.jpg)     

# Acknowledgements
This was inspired by Martin Wimpress' [Mate Optimus](https://github.com/ubuntu-mate/mate-optimus) project and is a fork of openSUSE's [suseprime-appindicator](https://github.com/openSUSE/suseprime-appindicator) project.

It has been updated to work with the Optimus-Switch program by dglt1, links are in the requirements section, on laptops running Manjaro.

Thank you to the authors of the above programs.

New default icons and the program logo were crafted with love by SGS from the Manjaro Forums. You can find more of his wonderful work here: [GitHub](https://github.com/sgse), [GitLab](https://gitlab.com/SGSm/manjaro-wallpaper/), and [The Manjaro Forums](https://forum.manjaro.org/t/wallpaper-and-more-by-sgs/43181). Thank you so much for sharing your time and talent!

Thank you also goes to the members of the Manjaro forums who took the time to help me learn about and troubleshoot python. I truly do appreciate it.

# About

This is an indicator that resides in the system tray. It displays an icon that shows which graphics card, either nVidia or Intel, is in use, and allows the user to switch between the two via a GUI menu.

# Desktop Environments Supported

This program only supports Gnome using Wayland.

# Requirements
- The appropriate version of Optimus-Switch for your desktop envirnoment [Optimus-Switch Repositories](https://github.com/dglt1).
- libappindicator-gtk3 package from the Manjaro Community Repository.
- libappindicator-gtk2 package from the Manjaro Community Repository.
- libnotify package from the Manjaro Extra Repository.
- [Kstatusnotifieritem/appindicator](https://extensions.gnome.org/extension/615/appindicator-support/) extension. This "re-adds" the removed system tray. Without this extension enabled, the icon will not show in the top bar or the "system tray" section of Dash-to-Dock.

# Installation

#### Before installation, make a back-up of your system using your favorite back-up tool!!!

1. Install the version of Optimus-Switch for your chosen desktop environment.

2. Install libappindicator-gtk3 from the Manjaro Community Repository.
```
sudo pacman -S libappindicator-gtk3
```
3. Install libappindicator-gtk2 from the Manajro Community Repositry
```
sudo pacman -S libappindicator-gtk2
```
4. Install the libnotify package from the Manjaro Extra Repository.
```
sudo pacman -S libnotify
```
5. Clone this repository to your computer and go to its folder.
```
git clone https://github.com/linesma/manjaroptimus-appindicator.git
cd manjaroptimus-appindicator-gdm
```
6. Make the install script executable.
```
chmod a+x setupgn.py
```
7. Run the setup script.
```
sudo ./setupgn.py install
```

The setup script will then copy the files to the required directories and adjust their permissions as needed.

8. Once the install script has finished. Reboot the computer. Manjaro-Optimus Indicator GDM is set to autostart when the computer boots.

#### NOTE:

You need to RESTART your laptop to have the graphics card change take effect.

# Troubleshooting

Q. I am getting an error message saying "Removed /etc/systemd/system/graphical.target.wants/disable-nvidia.service" or "Created symlink...."

A. This is not an error. It is notifying the user that the "set-intel" and the "set-nvidia" scripts are changing a systemd service. The script has still run and changed the graphics card. To stop this notification, run the "setupgn.py" file. It will change the "set-intel" and "set-nvidia" scripts to stop these notifications. 

# Uninstall

#### Note: This will not uninstall the Optimus-Switch GPU solution. This only uninstalls this indicator program.

1. Open the terminal and type.
```
cd manjaroptimus-appindicator-gdm
```
2. Make the uninstall script executable.
```
chmod a+x uninstall-moi.sh
```
3. Run the uninstall script.
```
sudo ./uninstall-moi.sh
```
4. Reboot your laptop to have the changes take affect.


# Fun Stuff

I have included additional sets of icons in the "more-icons" folder. If you want to use one of these sets instead of the default, just copy the set you want into the '/usr/share/icons/hicolor/symbolic/apps'. For example:

```
sudo cp ~/manjaroptimus-appindicator/more-icons/set01/*.svg /usr/share/icons/hicolor/symbolic/apps
```
The original icons I used in the initial release are included in the folder "more-icons/set-original".
I will be adding more icon choices in the future.

Enjoy!!!
