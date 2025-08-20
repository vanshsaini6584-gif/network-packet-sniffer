from scapy.all import get_if_list

interfaces = get_if_list()
print("Available Network Interfaces:")
for iface in interfaces:
    print("-", iface)
