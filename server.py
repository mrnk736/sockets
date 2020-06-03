#!/usr/bin/env python

# -*- coding: utf-8 -*-

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#ip = 192.168.56.101
server_address = ('192.168.56.101', 5565)
sock.bind(server_address)





while True:
	data, address = sock.recvfrom(1024)
	print(data)
	if not data:
		break
	info = input("Server message: ")
	sock.sendto(info.encode(), address)
	if (info == "Bye" or info == "bye"):
		break
sock.close() 
