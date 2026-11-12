import socket

host = "example.com"
port = 443

try:
    with socket.create_connection(
        (host, port), timeout=5
    ):
        print("Connection successful")
except OSError as error:
    print("Connection failed:", error)
