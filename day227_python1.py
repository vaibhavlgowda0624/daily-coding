import socket

domain = "example.com"

try:
    ip_address = socket.gethostbyname(domain)
    print("Domain:", domain)
    print("IP address:", ip_address)
except socket.gaierror:
    print("Unable to resolve domain")
