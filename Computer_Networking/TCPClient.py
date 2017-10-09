# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 21:48:33 2017

@author:zexin

mail:yzxforwork@163.com
wechat:yangzexinlikewow
github:https://github.com/lllidan

You are not prepared
"""

from socket import *
serverName = 'servername'
servePort = 12000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,servePort))
sentence =input("input lowercase sentence:")
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print("From Server:"+str(modifiedSentence))
clientSocket.close()