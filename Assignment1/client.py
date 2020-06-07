import socket as s
import sys

clientSocket = s.socket(s.AF_INET, s.SOCK_STREAM)

host = sys.argv[1]
port = int(sys.argv[2])
page = sys.argv[3]

request = "GET /" + page + " HTTP/1.1\r\n"

#print("Connecting to " + sys.argv[1] + " at port " + str(sys.argv[2] + '.')
serverIP = s.gethostbyname(host)
clientSocket.connect((serverIP, port))
#print("Connected!")

clientSocket.sendall(request.encode())

initial = True
while (initial or reply != ''):
	initial = False
	reply = clientSocket.recv(4096)
	print(reply)

raw_input()

sys.exit()
