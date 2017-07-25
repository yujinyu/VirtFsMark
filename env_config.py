# -*- coding: UTF-8 -*-
import subprocess

def is_installed(pkg_name):
    state, stout = subprocess.getstatusoutput("dpkg --get-selections | grep " + pkg_name + " | awk \'{print $2}\'")
    if state == 0 and stout == "install":
        return True
    else:
        return False



def pkg_install(pkg_name):
    state, stout = subprocess.getstatusoutput("sudo apt-get install -y " + pkg_name)
    if state == 0:
        return True
    else:
        return False
