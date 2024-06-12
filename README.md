# Socket-based Port Scanner

**This version does not require Nmap**

This Python script is a simple port scanner that utilizes the Windows sockets API to scan for open ports on a specified IP address. It allows users to input an IP address and a range of ports to scan, and it reports back the status of each port (open or closed).

How it Works:

This scanner will attempt to establish a TCP connection to each port in the specified range and report back whether the port is open or closed

## Features

- Uses Python's built-in `socket` module for port scanning.
- Supports scanning of a range of ports or all ports.
- Provides a multithreaded scanning process for faster results.
- Gracefully handles user input errors and exceptions.

## Usage

1. Clone the repository:

git clone https://github.com/clommm/Socket-Port-Scanner.git

2. Navigate to the project directory:

cd (directory)

3. Run the script:

python3 socket_port_scanner.py (if this doesnt work, use: python3 socket_port_scanner.py instead)

4. Follow the on-screen instructions to input the IP address and port range to scan.

## Requirements

- Python 3.x
- Python pyfiglet

Install the required Python packages using pip:

pip install pyfiglet



