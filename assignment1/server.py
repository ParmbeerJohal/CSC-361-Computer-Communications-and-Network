#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
host = '142.104.74.80'
ports = [7878, 8787]
portIndex = 0
port = ports[0]

while True:
	try:
		serverSocket.bind((host, port))
		break
	except error:#socket.error
		portIndex += 1
		port = ports[portIndex]

serverSocket.listen(10)

while True:
	#Establish the connection
	print('Ready to serve at ' + host + ':' + str(port))
	connectionSocket, addr =  serverSocket.accept()

	try:
		message = connectionSocket.recv(4096)
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.readlines()

		#Send one HTTP header line into socket
		headerLine = "HTTP/1.1 200 OK"
		connectionSocket.sendall((headerLine + '\r\n\r\n').encode())

		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode())

	except IOError:
		#Send response message for file not found
		headerLine = "HTTP/1.1 404 Not Found"
		connectionSocket.sendall((headerLine + '\r\n\r\n').encode())

	except IndexError:
		pass

	connectionSocket.close()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
