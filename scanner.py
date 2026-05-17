import socket
import random

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55000))

ports = [22, 80, 443, 3306, 8080]

open_ports = [p for p in ports if random.choice([True, False])]

message = f"OPEN PORTS: {open_ports}"

client.send(message.encode())

response = client.recv(1024)

print("[SERVER RESPONSE]", response.decode())

client.close()