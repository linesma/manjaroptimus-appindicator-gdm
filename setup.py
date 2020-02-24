#!/usr/bin/python3

import os
from distutils.core import setup
from glob import glob

setup(name="manjaroptimus-appindicator",
      version="2.0.1",
      description="AppIndicator for optimus-switch-gdm",
      url='https://github.com/linesma/manjaroptimus-appindicator-gdm',
      author='Mark Lines',
      license='GPLv3',
      packages=["src/manjaroptimusindicator"],
      data_files=[
          ('/usr/local/bin/', ['src/uninstall/manjaroptimus-appindicator-uninstall.sh']),
          ('/usr/share/icons/hicolor/symbolic/apps/', ['src/icons/default/manjaroptimus-symbolic.svg', 'src/icons/default/manjaroptimus-intel-symbolic.svg', 'src/icons/default/manjaroptimus-nvidia-symbolic.svg']),
          ('/usr/share/manjaroptimus-appindicator/scripts/', ['src/scripts/pkexec_nvidia', 'src/scripts/pkexec_intel_x11', 'src/scripts/pkexec_intel_wayland', 'src/scripts/reboot.sh']),
          ('/usr/share/polkit-1/actions/', ['src/polkit/org.freedesktop.policykit.set-intel-x11.sh.policy', 'src/polkit/org.freedesktop.policykit.set-intel-wayland.sh.policy', 'src/polkit/org.freedesktop.policykit.set-nvidia.sh.policy']),
          ('/etc/xdg/autostart/', ['src/autostart/manjaroptimus-appindicator.desktop'])],
      scripts=["src/bin/manjaroptimus-appindicator"]
)

os.chmod ('/usr/local/bin/manjaroptimus-appindicator-uninstall.sh', 0o755)
os.chmod ('/etc/xdg/autostart/manjaroptimus-appindicator.desktop', 0o755)
os.chmod ('/usr/bin/manjaroptimus-appindicator', 0o755)
os.chmod ('/usr/share/manjaroptimus-appindicator/scripts/pkexec_nvidia', 0o755)
os.chmod ('/usr/share/manjaroptimus-appindicator/scripts/pkexec_intel_x11', 0o755)
os.chmod ('/usr/share/manjaroptimus-appindicator/scripts/pkexec_intel_wayland', 0o755)
os.chmod ('/usr/share/manjaroptimus-appindicator/scripts/reboot.sh', 0o755)


