#!/usr/bin/python

import platform

from helper import check_group, check_group_multiprocess
from pi import pi

print ("Starting search")

if platform.system() == 'Windows':
    check = check_group
else:
    check = check_group_multiprocess

group5_start = 2**1536 - 2**1472 - 1 + 2**64 * (pi(1406))
check(group5_start)

group14_start = 2**2048 - 2**1984 - 1 + 2**64 * (pi(1918))
check(group14_start)

group15_start = 2**3072 - 2**3008 - 1 + 2**64 * (pi(2942))
check(group15_start)

group16_start = 2**4096 - 2**4032 - 1 + 2**64 * (pi(3966))
check(group16_start)

group17_start = 2**6144 - 2**6080 - 1 + 2**64 * (pi(6014))
check(group17_start)

group18_start = 2**8192 - 2**8128 - 1 + 2**64 * (pi(8062))
check(group18_start)
