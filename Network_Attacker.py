# Importing all the sub liberies from scapy.all
from socket import timeout
from sys import flags
from scapy.all import *
from scapy.layers.inet import TCP, IP, Ether, ICMP
from scapy.layers.l2 import ARP

# Asking the user for target ip address
target = input("Please insert your target IP: ==> ")

# Creating variable that equals to all registered ports
Registered_Ports = range(1,1025)

# Creating an empty list by name Open_Ports
Open_Ports = []

# Creating scan port function with single argument followed by the name port
port = 22 
def ScanPort(port):
    src_port = RandShort()
    conf.verb = 0
    Syn_Pkt = sr1(IP(dst=target)/TCP(sport=src_port,dport=port,flags="S"), timeout=0.5)
    if Syn_Pkt:
        if Syn_Pkt.haslayer(TCP):
            if Syn_Pkt[1].flags == 0x12:
                sr(IP(dst=target)/TCP(sport=src_port,dport=port,flags="R"), timeout=2)
                return True
        else:
            return False
    else:
        return False
print(ScanPort(port))