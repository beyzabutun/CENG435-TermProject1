from socket import *
from socket import socket
import time
import ntplib
import struct
import math
serverPort = 25813
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
serverPort = 25811
serverSocket2 = socket(AF_INET, SOCK_DGRAM)
serverSocket2.bind(('', serverPort))
returnedList = list() #to save the sensor datas
statisticsList = list() #to save the end-to-end delays
print 'The server is ready to receive'
counter=0 #to count the number of received datas, its will be updating in each receiving
boool=True #to change receiving process between the router1 and router2
while 1:
        if boool==True:
                message, clientAddress = serverSocket.recvfrom(2048)
                index4=message.find('+') #to extract sending data
		c=ntplib.NTPClient()
	        response=c.request('ops.instageni.clemson.edu',version=3)
	        x=response.tx_time
                statisticsList.append(1000*(x-struct.unpack("d",message[index4+1:])[0])) #calculate end-to-end delay and insertion it into the list
        else:
                message, clientAddress = serverSocket2.recvfrom(2048)
                index4=message.find('+') #to extract sending data
		c=ntplib.NTPClient()
	        response=c.request('ops.instageni.clemson.edu',version=3)
	        x=response.tx_time
                statisticsList.append(1000*(x-struct.unpack("d",message[index4+1:])[0])) #calculate end-to-end delay and insertion it into the list
        boool= not boool #change the bool for next iteration
        index1=message.find('*') #to extract datas count which will be received totally and to extract data's itself
        index2=message.find('&') #to extract data's itself and index
        index3=message.find('+') #to extract data's index
        i=int(message[index2+1:index3]) #extracting data's index
        count=int(message[:index1]) #extracting datas count which will be received totally
        message2=message[index1+1:index2] #extracting data's itself
        returnedList.insert(i-1,message2) #inser the data to the given index
        counter+=1 #increase the received datas up to this time
        if counter==count: #checking whether we reached end of the datas or not; if we reach, we can print datas which were sent in source, in correct order and convserving input format
                temp = "Received Datas: "+returnedList[0] #to maintain commas to conserve input format
                for x in returnedList[1:]:
                        temp=temp+","+x #to add comma and then data
                print temp #output which is same with input
                # print 'Average end-to-end delay is ',sum(statisticsList)/len(statisticsList) #to plot the graph
                # print 'Variance of end-to-end delay is', sum((sum(statisticsList)/len(statisticsList) - x) ** 2 for x in statisticsList) / float(len(statisticsList) - 1) #to plot the graph
                #print 'Error is ',math.sqrt(sum((sum(statisticsList)/len(statisticsList) - x) ** 2 for x in statisticsList) / float(len(statisticsList) - 1))*1.96/math.sqrt(len(statisticsList)) #to plot the graph
                del returnedList[:] #to receive next new list of sensors
                del statisticsList[:] #to receive next new list of sensors
                counter=0 #to receive next new list of sensors
                boool=True #to receive next new list of sensors
        serverSocket.sendto(message, clientAddress)
