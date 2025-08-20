from scapy.all import get_if_list, get_if_addr

print("🟢 Interface List with IP Addresses:")
for iface in get_if_list():
    try:
        ip = get_if_addr(iface)
        print(f"{iface} --> IP: {ip}")
    except:
        print(f"{iface} --> [No IP assigned]")
