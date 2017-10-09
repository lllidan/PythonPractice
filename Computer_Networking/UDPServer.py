# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 21:01:35 2017

@author:zexin

mail:yzxforwork@163.com
wechat:yangzexinlikewow
github:https://github.com/lllidan

You are not prepared
"""

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("The server is ready to receive")
while True:
    message,clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage,clientAddress)
    