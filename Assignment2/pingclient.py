#Parm Johal
#Student Number: V00787710
#Lab 2
#pingclient.py

#Importing socket and time
from socket import *
import time as t


#Creating a socket
s = socket(AF_INET, SOCK_DGRAM)

#Create a message to send
ping_message = "hello world"

#sending ping message
pingnum = 1
while pingnum < 11:
	#This line sets the timeout for 1 second
	s.settimeout(1.0)

	destination = ("10.0.0.2", 12000)

	start_time = t.time()
	s.sendto(ping_message, destination)
	#try to receive a ping, if not received then exception occurs
	try:
		response, server = s.recvfrom(1024)
		end_time = t.time()
		interval = end_time - start_time
		print(response + ", " + str(pingnum) + ", " + str(interval))
	except timeout:
		print "Request timed out"

	pingnum += 1
