# General Info

Scapy is a tool written in Python for network packet manipulation.
We will use it to create a tool to make the man-in-the-middle attack.
With the python library Tkinter, we will display a graphical interface to make the usage more pleasant.

With this attack we will modify the ARP table entries of the victim and the gateway. In this way, our attacking machine will be able to place itself between the two. Following this, you can visualise the packets in traffic using Wireshark with the appropriate filters.

## Requirements

First of all, you need to install the requirements. On the current project folder, use :

`pip3 install -r requirements.txt`

Then, enable IP forwarding on your machine :

1. If you are on Windows, open PowerShell with Admin rights:

	`Set-Location HKLM:\`	
	
	`Set-ItemProperty -Path "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" -Name "IPEnableRouter" -Value "1"`

	To disable forwarding : `Set-ItemProperty -Path "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" -Name "IPEnableRouter" -Value "0"`

2. If you are on Linux :

	`echo 1 > /proc/sys/net/ipv4/ip_forward`

	To disable forwarding : `echo 0 > /proc/sys/net/ipv4/ip_forward`

## Run

Before runing the program, you can display the ARP table to see adresses. You can compare result after using this tool.
To see it : `arp -a`


Run the program : `python3 mitm-arp.py`