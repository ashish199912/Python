import subprocess
import platform

def change_mac(interface, new_mac):
    if platform.system() == "Linux":
        print("[+] Changing MAC address for " + interface + " to " + new_mac)
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["ifconfig", interface, "up"])
    elif platform.system() == "Windows":
        print("[+] Changing MAC address for " + interface + " to " + new_mac)
        subprocess.call(["netsh", "interface", "set", "interface", "physicaladdress=" + new_mac, "name=" + interface])

def change_ip(interface, new_ip):
    if platform.system() == "Linux":
        print("[+] Changing IP address for " + interface + " to " + new_ip)
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "inet", new_ip])
        subprocess.call(["ifconfig", interface, "up"])
    elif platform.system() == "Windows":
        print("[+] Changing IP address for " + interface + " to " + new_ip)
        subprocess.call(["netsh", "interface", "ipv4", "set", "address", "name=" + interface, "static", new_ip])

def restore_mac(interface):
    if platform.system() == "Linux":
        print("[+] Restoring original MAC address for " + interface)
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", "restore"])
        subprocess.call(["ifconfig", interface, "up"])
    elif platform.system() == "Windows":
        print("[+] Restoring original MAC address for " + interface)
        subprocess.call(["netsh", "interface", "set", "interface", "physicaladdress=", "name=" + interface])

def restore_ip(interface):
    if platform.system() == "Linux":
        print("[+] Restoring original IP address for " + interface)
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "inet", "restore"])
        subprocess.call(["ifconfig", interface, "up"])
    elif platform.system() == "Windows":
        print("[+] Restoring original IP address for " + interface)
        subprocess.call(["netsh", "interface", "ipv4", "set", "address", "name=" + interface, "dhcp"])

interface = input("Enter interface name: ")

while True:
    print("1. Change MAC address")
    print("2. Change IP address")
    print("3. Restore original MAC address")
    print("4. Restore original IP address")
    print("5. Quit")
    choice = input("Enter choice: ")
    if choice == "1":
        new_mac = input("Enter new MAC address: ")
        change_mac(interface, new_mac)
    elif choice == "2":
        new_ip = input("Enter new IP address: ")
        change_ip(interface, new_ip)
    elif choice == "3":
        restore_mac(interface)
    elif choice == "4":
        restore_ip(interface)
    elif choice == "5":
        break
    else:
        print("Invalid choice")

