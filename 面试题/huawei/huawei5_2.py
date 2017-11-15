# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:53:50 2017

@author: mywow
question:
计算重复字符个数
【题目描述】输入一行字符串。如果字符是英文字母，则输出为输入的英文字符+连续出现的次数 ，例如
“ABBCCCC”-> “A1B2C4”；否则，丢弃该字符，不输出。
输入：
输入的字符串，长度小于1024
输出：
输入的英文字符以及其重复的次数
样例输入：
ABBC67%%%CCCAA99
"""

strings = input("请输入一行字符串")
flag = True
stringsList = []
for i in strings:
    if ord(i)<65 or ord(i)>90 and ord(i)<97 or ord(i)>122:
        flag = False
        print("字符"+ i +"不是字符")
    stringsList.append(i)
num = 0
outputs = ""
stringsListCopy = [i for i in stringsList]
if flag == True:
    for p in stringsList:
        num = 0
        for q in stringsListCopy:
            if p == q:
                num = num + 1
#                stringsListCopy.remove(q)
                
        for i in range(num):
            stringsListCopy.remove(p)
        if num != 0:
            outputs = outputs + p + str(num)

print(outputs)
        
        
        
        

        
        
        
