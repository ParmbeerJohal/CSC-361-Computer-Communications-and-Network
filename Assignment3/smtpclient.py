#Parm Johal
#Student Number: V00787710
#Lab 3
#smtpclient.py

from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.uvic.ca", 25)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# Send MAIL FROM command and print server response.
mail_from = "MAIL FROM: parmbeerjohal@gmail.com \r\n"
clientSocket.send(mail_from.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')


# Send RCPT TO command and print server response. 
rcpt_to = "RCPT TO: russelljohal@gmail.com \r\n"
clientSocket.send(rcpt_to.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')


# Send DATA command and print server response. 
data = "DATA: \r\n"
clientSocket.send("DATA".encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '250':
    print('250 reply not received from server.')

# Send message data.
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())

# Send QUIT command and get server response.
clientSocket.send("Quit\r\n".encode())
serverResponse = clientSocket.recv(1024).decode()
print(serverResponse)
if serverResponse[:3] != '250':
    print('250 reply not received from server.')
clientSocket.close()
