from sys import flags
from scapy.all import *
from scapy.layers.inet import TCP, IP, Ether, ICMP
from scapy.layers.l2 import ARP
packet1 = (IP(dst="192.168.1.49")/TCP(dport=80, flags="S"))
ans, unans = sr(packet1)
print("------------------------------------")
print(ans)
print("------------------------------------")
print(unans)