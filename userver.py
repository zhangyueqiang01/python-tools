#!/usr/bin/python

from socket import *
from time import ctime

HOST=''
PORT=2223
BUFSIZ=1024
ADDR=(HOST,PORT)

udpSerSock=socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for connection....')
    data,addr=udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto('[%s] %s' %(ctime(),data), addr)
    print('....received from and returned to:' ,addr)

udpSerSock.close()