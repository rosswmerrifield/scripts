#!/bin/bash

int=$@

if [[ -z "$int" ]]
then
	echo "error: no interface specified"
	echo "usage: netinfo <int>"
	echo "defaulting to  en0"
	int="en0"
fi

ipaddr=`ifconfig $int | grep -Ev inet6 | awk '/inet/ {print$2}'`

if [[ -z "$ipaddr" ]]
then
	echo "error: there does not seem to be an address configured on this interface ($int)"
	exit 1
fi

hexmask=`ifconfig $int | grep -Ev inet6  | awk '/inet/ {print $4}' | sed -e 's/0x//'`
h1=${hexmask%????}
h2=${hexmask#????}
netmask=`printf "%d.%d.%d.%d\n" 0x${h1%??} 0x${h1#??} 0x${h2%??} 0x${h2#??}`
gateway=`netstat -rn |  awk '/default/ {print $2}' | tr '\n' '\ '`
speed=`ifconfig $int |  awk '/media/ {print $3}' | sed -e 's/(//'`
duplex=`ifconfig $int | awk '/media/ {print $4}' | sed -e 's/)//'`
dns=`cat /etc/resolv.conf | awk '/nameserver/ {print $2}' | tr '\n' '\ '`

echo "      IP address:	$ipaddr"
echo "     subnet mask:	$netmask"
echo " default gateway:	$gateway"
echo "      DNS server:	$dns"
echo "    speed/duplex:	$speed $duplex"
