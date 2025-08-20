from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.packet import Raw

def analyze_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print("\n[+] Packet Mila:")
        print(f"    From: {ip_layer.src} --> To: {ip_layer.dst}")
        print(f"    Protocol: {ip_layer.proto}")

        if TCP in packet:
            print("    TCP Packet")
        elif UDP in packet:
            print("    UDP Packet")
        elif ICMP in packet:
            print("    ICMP Packet")

        if packet.haslayer(Raw):
            print("    Payload:", packet[Raw].load)

# 👇 Yahan correct interface lagaya gaya hai:
iface = r"\Device\NPF_{A44388C5-891B-49E3-8823-82A382052A09}"

print("🟢 Sniffer Start ho raha hai...")
sniff(prn=analyze_packet, iface=iface, count=10)
