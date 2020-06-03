#!/usr/bin/env python

# -*- coding: utf-8 -*-

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.56.101', 5565)
while True:
    str_in = input("Message: ")
    sock.sendto(str_in.encode(), server_address)
    if (str_in == "Bye" or str_in == "bye"):
        break
    data = sock.recvfrom(1024)
    print('Data from server:\n', data)

sock.close 