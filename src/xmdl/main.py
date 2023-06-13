import gethttp

import os
import psutil
import pipeline.pipelineAUR
import pipeline.pipelinePyPI

source = input("What is the package source ? (aur, AirOS, snap, flatpak, inscription) (TYPE AS WRITTEN): ")
pkg = input("Package: ")
action = input("Action: ")
userDo = input("{} {}: ? (y/n)".format(action, pkg))

if (source == "aur") :
    gethttp.get_package_aur()
elif (source == "AirOS") :
    gethttp.get_package()
elif (source == "inscription") :
    gethttp.GetInScription()
else:
    print("Unknown awnser. terminating script")

if (userDo == "y") :
    print("{} undergoing  {} using {}. Hang tight, this may take a while".format(pkg, action, source))
else:
    print("Unknown or negative awnser. no changes made to {}, using System Partition MOUNPOINT /".format(pkg))
