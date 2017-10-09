# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 20:01:14 2017

@author:zexin

mail:yzxforwork@163.com
wechat:yangzexinlikewow
github:https://github.com/lllidan

You are not prepared
"""

from socket import *
serverName = 'hostname'
serverPort =12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(),(serverName,serverPort))
modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage)
clientSocket.close()