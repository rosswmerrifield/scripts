#!/usr/bin/env python

import optparse
import os
from sys import stdout
from time import sleep

parser = optparse.OptionParser()
parser.add_option("-i", action="store", type="string", dest="interface",\
 default="en0", help="specify an interface with: -i <int>")

(options, args) = parser.parse_args()

dhcp = "sudo ipconfig set %s DHCP" % options.interface 

if options.interface == "en0":
	os.system("sudo networksetup -setdhcp ethernet")
elif options.interface == "en1":
	os.system("sudo networksetup -setdhcp Wi-Fi")
else:
	print "Cannot determine valid interface (en0 or en1)"
	quit()

os.system(dhcp)

print "Waiting 10 seconds for dhcp offer..."

for i in range(1,10):
	stdout.write("\r%d" % i)
	stdout.flush()
	sleep(1)

stdout.write("\n")

cmd="netinfo %s" % options.interface
addr= os.system(cmd)

quit()
