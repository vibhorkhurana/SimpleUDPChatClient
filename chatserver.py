#!/usr/bin/python

import socket
from select import select
serv=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serv.bind(('',6667))
def run():
	while 1:
		data,addr=serv.recvfrom(6556)
		print "Data Received: "+data
		st=raw_input("Enter Data to Send: ")
		serv.sendto(st,('127.0.1.1',6556))
	serv.close()
run()
