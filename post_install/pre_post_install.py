


import os
import subprocess


print("Arm removal of rebornos user using a service")
subprocess.run(["systemctl", "enable", "oemcleanup.service"])
subprocess.run("rm /etc/sddm.conf.d/autologin.conf", shell=True)
rm_calamares_service= '''
[Unit]
Description=Remove Calamares 

[Service]
Type=oneshot
ExecStart=/bin/pacman -Rncsu --noconfirm calamares-core calamares-configuration && systemctl disable remove-calamares.service

[Install]
WantedBy=multi-user.target
'''
with open("/usr/lib/systemd/system/remove-calamares.service", "w") as f:
    f.write(rm_calamares_service)
subprocess.run(["systemctl", "enable", "remove-calamares.service"])
subprocess.run(["rm", "/etc/sddm.conf.d/autologin.conf"])

if os.path.exists("/tmp/lxqt-user"):
    print("LXQt detected...")
else:
    subprocess.run(['systemctl', 'disable', 'sddm.service'])
    print("LXQt not detected...")
    print("Removinging LXQt...")
    subprocess.run(["pacman", "-Rnscu","rebornos-cosmic-lxqt", "--noconfirm",],shell=True)
    print("LXQt removed...")