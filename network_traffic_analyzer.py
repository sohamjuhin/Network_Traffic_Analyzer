from scapy.all import *

# Function to analyze network traffic
def analyze_traffic(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        print("Source IP: {}, Destination IP: {}, Protocol: {}".format(src_ip, dst_ip, protocol))

# Usage example
sniff(filter="ip", prn=analyze_traffic)
