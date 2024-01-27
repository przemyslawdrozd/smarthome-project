import socket
import time
# Server IP and Port
server_ip = '192.168.0.102'  # listens on all interfaces
server_port = 12345

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the IP and port
sock.bind((server_ip, server_port))

print("UDP server listening...")

try:
    while True:
        # Receive data from client
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        print(time.time())
        print(f"Received message: {data.decode()} from {addr}")
except KeyboardInterrupt:
    print("UDP Server stopped")
finally:
    sock.close()
