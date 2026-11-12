import socket

hostname = socket.gethostname()

print("Computer name:", hostname)

try:
    print("Local IP:", socket.gethostbyname(hostname))
except socket.gaierror:
    print("IP address unavailable")
