# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 22:46:33 2017

@author:zexin

mail:yzxforwork@163.com
wechat:yangzexinlikewow
github:https://github.com/lllidan

input:a length of code
ouput:a string consist of numbers and Words(both capital and small letter)  
You are not prepared
"""
import random
source=[]
for i in range(26):
    source.append(chr(i+65))
for i in range(26):
    source.append(chr(i+97))
for i in range(10):
    source.append(chr(i+48))

num=int(input("请输入要生成的密码长度："))
code=[]
for i in range(num):
    code.append(source[random.randint(0,(len(source)-1))])
    
for i in code:
    print(i,end='')
