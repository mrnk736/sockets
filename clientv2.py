import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.56.101', 5565)

sock.sendto("Message".encode("ascii"), server_address)

data = sock.recvfrom(1024)
print('Data from server:\n', data)

sock.close