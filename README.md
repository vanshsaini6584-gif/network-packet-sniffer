# 🕵️‍♂️ Network Packet Sniffer using Python (Scapy)

This repository contains a simple but powerful **Network Packet Sniffer** tool built using **Python** and **Scapy**. It helps in monitoring and analyzing real-time network traffic from selected network interfaces.

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `sniffer.py` | Main sniffer script to capture and analyze network packets |
| `list_interfaces.py` | Lists all available network interfaces |
| `detailed_interfaces.py` | Lists network interfaces along with assigned IP addresses |

---

## 🚀 Features

✅ Captures live network packets  
✅ Supports TCP, UDP, and ICMP protocols  
✅ Displays source & destination IP, protocol, and payload  
✅ Select specific network interface for sniffing  
✅ Easy-to-understand output

---

## 🛠️ Requirements

- Python 3.x
- [Scapy](https://scapy.net/)

Install Scapy via pip:

```bash
pip install scapy
```

---

## 🧪 How to Use

### 1️⃣ List Available Interfaces

```bash
python list_interfaces.py
```

### 2️⃣ List Interfaces with IP Addresses

```bash
python detailed_interfaces.py
```

> ℹ️ Choose the correct interface string for your system. For example:  
`\\Device\\NPF_{A44388C5-891B-49E3-8823-82A382052A09}`

### 3️⃣ Start the Sniffer

Update the `iface` variable in `sniffer.py` with your selected interface and run:

```bash
python sniffer.py
```

---

## 📸 Sample Output

```
🟢 Sniffer Start ho raha hai...

[+] Packet Mila:
    From: 192.168.1.10 --> To: 142.250.67.78
    Protocol: 6
    TCP Packet
    Payload: b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n'
```

---

## 📌 Notes

- Make sure to run the script with administrator/root privileges.
- Works best on Windows with Npcap installed.

---

## 👨‍💻 Author

Created by [Your Name Here]  
Feel free to fork, contribute, or open issues!