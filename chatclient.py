#!/usr/bin/env python
from socket import *
from select import select
import sys

print gethostname()[:6]

HOST = gethostbyname(gethostname()) #it will take system hostname IP
print "your current ip :-> "+HOST
SERV = raw_input('Enter Receiver ip')
PORT = int(raw_input('Enter Port'))
USER = gethostname()[:6] # to get the system Name
sender = socket(AF_INET, SOCK_DGRAM)
receiver = socket(AF_INET, SOCK_DGRAM)
receiver.bind((HOST, PORT))
def run():
	while 1:
		st = raw_input("Enter Text to send: ")
		sender.sendto(st,(SERV,6667))
		data,addr=receiver.recvfrom(6667)
		print "Data Received: "+data

	sender.close;
	receiver.close()
run()
