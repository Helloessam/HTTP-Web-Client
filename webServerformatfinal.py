#import socket module
from socket import *
#import pickle
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#serverIP = ""
#serverIP = gethostbyname(gethostname())
#serverIP = "127.0.0.1"
serverIP = "localhost"
serverPort = 12345
print("Server IP: {serverIP} , Server Port: {serverPort}")
serverSocket.bind((serverIP,serverPort))
serverSocket.listen(1)
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print("A client with address : {addr} has just connected")
    try:
        message = connectionSocket.recv(2048)
        #print(message)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(header.encode())
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        header = "HTTP/1.1 404 Not Found\r\n"
        connectionSocket.send(header.encode())
        #Close client socket
        connectionSocket.close()

    #serverSocket.close()
