from socket import *
import time
import ntplib
import struct
serverName = '10.10.1.2' #one of the broker's ip
serverPort = 25814 
sentence = raw_input('Sensor data:') #input seperated by comma without any space between (e.g., 1,2,3)
datas=map(str,sentence.split(",")) #create a python list from sensor datas which are seperated by comma 
i=0 #to indicate the index of list elements, this will increase by one in each iteration of following 'for iteration'
k=len(list(datas)) #length of the list which will be append to each data to use in destination to preserve order of sended datas
for data in datas:
        i=i+1
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName,serverPort))
	c=ntplib.NTPClient()
        response=c.request('ops.instageni.clemson.edu',version=3)
        x=response.tx_time #current time, which will help us while calculating the end-to-end delay in destination
        data=str(k)+'*'+data+'&'+str(i)+'+'+struct.pack("d",x) # we used *, & and + seperation symbol to seperate length of datas, data's itself, data's index and sending time
        clientSocket.send(data) #send to broker
        data2 = clientSocket.recv(1024)
        clientSocket.close()

