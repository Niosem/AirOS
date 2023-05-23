import gethttp

import os
import psutil

pkg = input("Package: ")
action = input("Action: ")
userDo = input("{} {}: ? (y/n)".format(action, pkg))

if (userDo == "y") :
    print("{} undergoing  {}. Hang tight, this may take a while".format(pkg, action))
    gethttp.get_package_aur()
else:
    print("Unknown or negative awnser. no changes made to {}, using System Partition".format(pkg))
