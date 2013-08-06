#!/usr/bin/env python

import os

baudRate = raw_input("What baud rate would you like to use? \n>")

if not baudRate:
	baudRate = "9600"

answer = raw_input("Would you like to launch the TFTP server? (yes or no) \n>")

if not answer:
	answer = "yes"

launchTftp = "/Applications/TftpServer.app/Contents/MacOS/TftpServer &"
launchScreen = "screen /dev/tty.usbserial %s" % baudRate

if answer == "yes":
	os.system(launchTftp)
elif answer == "y":
	os.system(launchTftp)
else:
	pass

os.system(launchScreen)

quit()
