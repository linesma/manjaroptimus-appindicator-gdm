#!/usr/bin/python3

import os
import signal
import json
import gi
import gettext

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')

from gi.repository import Gtk as gtk
from gi.repository import GLib as glib
from gi.repository import Gio as gio
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify

gettext.bindtextdomain('manjaroptimusindicator', '/usr/share/locale')
gettext.textdomain('manjaroptimusindicator')
_ = gettext.gettext

APPINDICATOR_ID = 'manjaroptimusindicator'

intel_x11_notif = ('Switching to the Intel iGPU (X11)')
intel_wayland_notif = ('Switching to the Intel iGPU (wayland)')
nvidia_notif = ('Switching to the nVidia GPU')
reboot_notif = ('Please reboot for changes to take effect')
reboot_notifb = ('Your system will now reboot')
error_head = ('Error occured')
session = os.environ['XDG_SESSION_TYPE']

drivers = {
    'nvidia corporation': '/usr/share/icons/hicolor/symbolic/apps/manjaroptimus-nvidia-symbolic.svg',
    'intel open source technology center': '/usr/share/icons/hicolor/symbolic/apps/manjaroptimus-intel-symbolic.svg',
    'intel': '/usr/share/icons/hicolor/symbolic/apps/manjaroptimus-intel-symbolic.svg',
    'other': '/usr/share/icons/hicolor/symbolic/apps/manjaroptimus-symbolic.svg',
}

def check_current(drivers):
    import subprocess
    try:
        proc = subprocess.Popen(['glxinfo','-B' ], text=True, stdout = subprocess.PIPE)
    except FileNotFoundError:
        return 'other'  # glxinfo not installed
    output = str(proc.communicate()[0]).split("\n")
    # or we can use `re`
    output = [ s.split(':')[1].strip().lower() for s in output if 'OpenGL vendor string' in s ]
    print(output) # debug
    for s in output:
        # list is not hard coded here, but use keys in array
        print('find', s, 'in', drivers.keys(), "...?" ) # debug
        if s in drivers.keys():
            return s
    return 'other' # not found

def main():
    if (check_current(drivers) == 'nvidia corporation'):
        icon = '/usr/share/icons/hicolor/symbolic/apps/manjaroptimus-nvidia-symbolic.svg'
    elif (check_current(drivers) == 'intel open source technology center' or check_current(drivers) == 'intel'):
        icon = '/usr/share/icons/hicolor/symbolic/apps/manjaroptimus-intel-symbolic.svg'
    else:
        icon = '/usr/share/icons/hicolor/symbolic/apps/manjaroptimus-symbolic.svg'
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, icon, appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    notify.init(APPINDICATOR_ID)
    gtk.main()

def build_menu():
    menu = gtk.Menu()
    if (check_current(drivers) != 'nvidia corporation'):
        item_nvidia = gtk.MenuItem.new_with_label(_('Switch to nVidia GPU and reboot'))
        item_nvidia.connect('activate', nvidia)
        menu.append(item_nvidia)
        if (session != 'x11'):
            item_intel_x11 = gtk.MenuItem.new_with_label(_('Switch to Intel iGPU (X11) and reboot'))
            item_intel_x11.connect('activate', intel_x11)
            menu.append(item_intel_x11)
        elif (session != 'wayland'):
            item_intel_wayland = gtk.MenuItem.new_with_label(_('Switch to Intel iGPU (wayland) and reboot'))
            item_intel_wayland.connect('activate', intel_wayland)
            menu.append(item_intel_wayland)
    if (check_current(drivers) != 'intel open source technology center' and check_current(drivers) != 'intel'):
        item_intel_x11 = gtk.MenuItem.new_with_label(_('Switch to Intel iGPU (X11) and reboot'))
        item_intel_x11.connect('activate', intel_x11)
        menu.append(item_intelb_x11)
        item_intel_wayland = gtk.MenuItem.new_with_label(_('Switch to Intel iGPU (wayland) and reboot'))
        item_intel_wayland.connect('activate', intel_wayland)
        menu.append(item_intelb_wayland) 
    menu.show_all()
    return menu

def nvidia(_):
    result, output, error, status = glib.spawn_command_line_sync('/usr/share/manjaroptimus-appindicator/scripts/pkexec_nvidia')
    if (error):
        notify.Notification.new(error_head, error.decode("utf-8"), 'dialog-warning').show()
    elif (result):
        notify.Notification.new(nvidia_notif, reboot_notifb, '/usr/share/icons/hicolor/symbolic/apps/manjaroptimus-nvidia-symbolic.svg').show()
        glib.spawn_command_line_sync('/usr/share/manjaroptimus-appindicator/scripts/reboot.sh')
    else:
        notify.Notification.new(error_head, output.decode("utf-8"), 'dialog-warning').show()

def intel_x11(_):
    result, output, error, status = glib.spawn_command_line_sync('/usr/share/manjaroptimus-appindicator/scripts/pkexec_intel_x11')
    if (error):
        notify.Notification.new(error_head, error.decode("utf-8"), 'dialog-warning').show()
    elif (result):
        notify.Notification.new(intel_x11_notif, reboot_notifb, '/usr/share/icons/hicolor/symbolic/apps/manjaroptimus-intel-symbolic.svg').show()
        glib.spawn_command_line_sync('/usr/share/manjaroptimus-appindicator/scripts/reboot.sh')
    else:
        notify.Notification.new(error_head, output.decode("utf-8"), 'dialog-warning').show()

def intel_wayland(_):
    result, output, error, status = glib.spawn_command_line_sync('/usr/share/manjaroptimus-appindicator/scripts/pkexec_intel_wayland')
    if (error):
        notify.Notification.new(error_head, error.decode("utf-8"), 'dialog-warning').show()
    elif (result):
        notify.Notification.new(intel_wayland_notif, reboot_notifb, '/usr/share/icons/hicolor/symbolic/apps/manjaroptimus-intel-symbolic.svg').show()
        glib.spawn_command_line_sync('/usr/share/manjaroptimus-appindicator/scripts/reboot.sh')
    else:
        notify.Notification.new(error_head, output.decode("utf-8"), 'dialog-warning').show()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
