#!/usr/bin/env python

from scapy.all import *
pcap = rdpcap("capture.pcap")
flag = []
for p in pcap[UDP]:
	try:
		if ( p[IP].src == "10.0.0.2" and p[IP].dst == "10.0.0.12" ):
			flag.append(p[Raw].load)
	except IndexError:
		continue

print(''.join(flag))