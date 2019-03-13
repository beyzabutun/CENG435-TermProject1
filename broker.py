from socket import *
serverPort = 25814
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The broker is ready'
while 1:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024)
        index=sentence.find('+') #to extract the index number of data
        sentence2=sentence[:index]
        if int(sentence2[-1:])%2==1: #if its index odd then forward it to the router
                serverName = '10.10.2.2' #one of the router1's ip
                serverPort = 25810
                clientSocket = socket(AF_INET, SOCK_DGRAM)
                clientSocket.sendto(sentence,(serverName, serverPort))
                modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        else: #if its index even then forward it to the router2
                serverName = '10.10.4.2' #one of the router2's ip
                serverPort = 25812
                clientSocket = socket(AF_INET, SOCK_DGRAM)
                clientSocket.sendto(sentence,(serverName, serverPort))
                modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        connectionSocket.close()

