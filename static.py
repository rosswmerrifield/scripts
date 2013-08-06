#!/usr/bin/env python

import subprocess

intr = raw_input("Interface:\n> ")
addr = raw_input("IP Address:\n> ")
mask = raw_input("Subnet Mask:\n> ")
gate = raw_input("Default Gateway (optional):\n> ")
dns = raw_input("DNS Server (optional):\n> ")

subprocess.call(["sudo", "cp", "/etc/resolv.conf", "/tmp/resolv.conf.backup"])

if intr == "en0":
	subprocess.call(["sudo", "networksetup", "-setmanual", "ethernet", addr, mask, gate])
elif intr == "en1":
	subprocess.call(["sudo", "networksetup", "-setmanual", "Wi-Fi", addr, mask, gate])
else:
	print "no valid interface specified (en0 or en1)"
	quit()

if len(dns) != 0:
	if intr=="en0":
		subprocess.call(["sudo", "networksetup", "-setdnsservers", "ethernet", dns])
	elif intr=="en1":
		subprocess.call(["sudo", "networksetup", "-setdnsservers", "Wi-FI", dns])
else:
	subprocess.call(["sudo", "mv", "/tmp/resolv.conf.backup", "/etc/resolv.conf"])

quit()
