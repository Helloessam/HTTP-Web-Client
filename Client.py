
from socket import *
import sys

serverIP = raw_input("Enter the host : ")
serverPort = raw_input("Your port: ")
filename = raw_input("Your filename: ")

host_port = "%s:%s" %(serverIP,serverPort)
ClientSocket = socket(AF_INET,SOCK_STREAM)
ClientSocket.connect((serverIP,int(serverPort)))
header = {"GET /%s HTTP/1.1" %(filename) }
ClientSocket.send("%s\r\n\r\n" %(header))

output=""
response_message=ClientSocket.recv(1024)
while response_message:
	output += response_message
	response_message = ClientSocket.recv(1024)

ClientSocket.close()
print "file content:",output
