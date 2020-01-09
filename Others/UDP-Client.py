import socket

target_host = "127.0.0.1"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host_config = (target_host, target_port)

client.sendto("AAABBBCCC", host_config)

data, address = client.recvfrom(4096)

print(data)