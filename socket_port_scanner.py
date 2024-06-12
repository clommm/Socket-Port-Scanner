import socket
import ipaddress
import re
import pyfiglet
import concurrent.futures
import sys
from datetime import datetime

port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

while True:
    ip_add_entered = input("\nPlease enter the IP address that you want to scan: ")
    try:
        ip_address_obj = ipaddress.ip_address(ip_add_entered)
        print("You entered a valid IP address.")
        break
    except ValueError:
        print("You entered an invalid IP address")

while True:
    print("Please enter the range of ports you want to scan in format: <int>-<int> (e.g., 60-120) or type 'all' to scan all ports")
    port_range = input("Enter port range: ").strip().lower()
    if port_range == "all":
        port_min = 0
        port_max = 65535
        break
    port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

def scan_port(port):
    try:
        # Create a new socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set timeout for connection attempt
        s.settimeout(1)
        # Attempt to connect to the target IP and port
        result = s.connect_ex((ip_add_entered, port))
        # Check if connection was successful
        if result == 0:
            return f"Port {port} is open"
        else:
            return f"Port {port} is closed"
    except Exception as e:
        return f"Cannot scan port {port}. Reason: {e}"
    finally:
        # Close the socket
        s.close()

# Add Banner
print("-" * 50)
print("Scanning Target: " + ip_add_entered)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)

try:
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, port) for port in range(port_min, port_max + 1)]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
except KeyboardInterrupt:
    print("\nExiting Program !!!!")
    sys.exit()
except Exception as e:
    print(f"\nAn error occurred: {e}")
    sys.exit()
