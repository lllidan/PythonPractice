# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 22:12:59 2017

@author:zexin

mail:yzxforwork@163.com
wechat:yangzexinlikewow
github:https://github.com/lllidan

You are not prepared
"""

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket,addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
