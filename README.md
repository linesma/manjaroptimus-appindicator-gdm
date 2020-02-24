<img src="https://github.com/linesma/manjaroptimus-appindicator-gdm/blob/master/media/logo/manjaroptimus-logo02b.png" align="left" width="256" />

# manjaroptimus-appindicator-gdm
## Indicator and GUI switch for optimus-switch-gdm.
</br>

![Manjaro-Optimus Indicator](https://github.com/linesma/manjaroptimus-appindicator-gdm/blob/master/media/screenshots/Flow3.jpg)     

# Acknowledgements
This was inspired by Martin Wimpress' [Mate Optimus](https://github.com/ubuntu-mate/mate-optimus) project and is a fork of openSUSE's [suseprime-appindicator](https://github.com/openSUSE/suseprime-appindicator) project.

It has been updated to work with the optimus-switch program by dglt1 on laptops running Manjaro.

Thank you to the authors of the above programs.

New default icons and the program logo were crafted with love by SGS from the Manjaro Forums. You can find more of his wonderful work here: [GitHub](https://github.com/sgse), [GitLab](https://gitlab.com/SGSm/manjaro-wallpaper/), and [The Manjaro Forums](https://forum.manjaro.org/t/wallpaper-and-more-by-sgs/43181). Thank you so much for sharing your time and talent!

Thank you also goes to the members of the Manjaro forums who took the time to help me learn about and troubleshoot python. I truly do appreciate it.

# About

This is an indicator that resides in the system tray. It displays an icon that shows which graphics card, either nVidia or Intel, is in use, and allows the user to switch between the two via a GUI menu. No matter which Desktop-Environment is being used. 

# Desktop Environments Supported

This version of manjaroptimus-appindicator only supports GNOME Display Manager.
For other desktop environments see https://github.com/linesma/manjaroptimus-appindicator


# Requirements
- [optimus-switch-gdm](https://github.com/likeadoc/optimus-switch-gdm)
- libappindicator-gtk3 package from the Manjaro Community Repository.
- libappindicator-gtk2 package from the Manjaro Community Repository.
- libnotify package from the Manjaro Extra Repository.
- [Kstatusnotifieritem/appindicator](https://extensions.gnome.org/extension/615/appindicator-support/) extension.

# Installation

#### Before installation, make a back-up of your system using your favorite back-up tool!!!

1. Install optimus-switch-gdm.

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
5. Clone this repository to your computer.
```
git clone https://github.com/linesma/manjaroptimus-appindicator-gdm.git
cd manjaroptimus-appindicator
```

6. Make the install script executable.
```
chmod a+x setup.py
```

7. Run the setup script.
```
sudo ./setup.py install
```

The setup script will then copy the files to the required directories and adjust their permissions as needed.

8. Once the install script has finished, reboot your computer. manjaroptimus-appindicator-gdm is set to autostart when the computer boots.


#### NOTE:

You need to RESTART your laptop to have the graphics card change take effect.

# Uninstall

#### Note: This will not uninstall optimus-switch-gdm. This only uninstalls this indicator program.

1. Run the uninstall script.
```
sudo manjaroptimus-appindicator-uninstall.sh
```
2. Reboot your laptop to have the changes take affect.


# Fun Stuff

There are additional sets of icons included in the "icons" folder. If you want to use one of these sets instead of the default, just copy the set you want to '/usr/share/icons/hicolor/symbolic/apps' once installed. For example:

```
sudo cp ~/manjaroptimus-appindicator-gdm/src/icons/set01/*.svg /usr/share/icons/hicolor/symbolic/apps
```
The original icons used in the initial release are included in the folder "icons/set06".
More icons choices may be added in the future.

Enjoy!!!
