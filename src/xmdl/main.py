import gethttp

import os
import psutil

source = input("What is the package source ? (aur, AirOS, snap, flatpak): ")
pkg = input("Package: ")
action = input("Action: ")
userDo = input("{} {}: ? (y/n)".format(action, pkg))

if (source == "aur") :
    gethttp.get_package_aur()
elif (source == "AirOS") :
    gethttp.get_package()

if (userDo == "y") :
    print("{} undergoing  {}. Hang tight, this may take a while".format(pkg, action))
else:
    print("Unknown or negative awnser. no changes made to {}, using System Partition".format(pkg))
