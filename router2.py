from socket import *
from socket import socket
serverPort = 25812
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print 'The router2 is ready'
while 1:
        message, clientAddress = serverSocket.recvfrom(2048)
        serverSocket.sendto(message, clientAddress)
        serverName = '10.10.3.2' #one of the destination ip
        serverPort = 25811
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        clientSocket.sendto(message,(serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
