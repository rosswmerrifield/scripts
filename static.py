#!/usr/bin/env python

import subprocess

int = raw_input("Interface:\n> ")
addr = raw_input("IP Address:\n> ")
mask = raw_input("Subnet Mask:\n> ")
gate = raw_input("Default Gateway (optional):\n> ")
dns = raw_input("DNS Server (optional):\n> ")

if int == "en0":
	subprocess.call(["sudo", "networksetup", "-setmanual", "ethernet", addr, mask, gate])
elif int == "en1":
	subprocess.call(["sudo", "networksetup", "-setmanual", "Wi-Fi", addr, mask, gate])
else:
	print "no valid interface specified (en0 or en1)"
	quit()

if len(dns) != 0:
	if int=="en0":
		subprocess.call(["sudo", "networksetup", "-setdnsservers", "ethernet", dns])
	elif int=="en1":
		subprocess.call(["sudo", "networksetup", "-setdnsservers", "Wi-FI", dns])
else:
	pass	

quit()
