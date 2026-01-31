#!/usr/bin/env python3
import platform
import sys
import os

if platform.system() != "Linux":
    exit("you are not on Linux! if you are on Windows, you should look at NotMyFault.")

if len(sys.argv) != 2:
    print("""no panic method selected!
listing available methods:
  sysrq - trigger sysrq crash (root only)
  modulepanic - load kernel module that triggers panic() (root only)
  modulebug - load kernel module that triggers BUG() (root only)""")
else:
    if sys.argv[1] == "sysrq":
        sysrq = open("/proc/sysrq-trigger", "w")
        sysrq.write("c")
        sysrq.close()
    elif sys.argv[1] == "modulepanic":
        os.system("modprobe snmf_panic")
    elif sys.argv[1] == "modulebug":
        os.system("modprobe snmf_bug")
    else:
        print("incorrect panic method")
