# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:38:43 2017

@author: mywow
question:
1、计算糖果
【题目描述】A,B,C三个人是好朋友,每个人手里都有一些糖果,我们不知道他们每个人手上具体有多少个糖果,
但是我们知道以下的信息：
A - B, B - C, A + B, B + C. 这四个数值.每个字母代表每个人所拥有的糖果数.
现在需要通过这四个数值计算出每个人手里有多少个糖果,即A,B,C。这里保证最多只有一组整数A,B,C满足
所有题设条件。
输入描述:
输入为一行，一共4个整数，分别为A - B，B - C，A + B，B + C，用空格隔开。
范围均在-30到30之间(闭区间)。
23
输出描述:
输出为一行，如果存在满足的整数A，B，C则按顺序输出A，B，C，用空格隔开，行末无空格。
如果不存在这样的整数A，B，C，则输出No
输入例子:
1 -2 3 4
输出例子:
2 1 3
"""

temp1=input().split()
temp1=[int(i) for i in temp1]
A=(temp1[0]+temp1[2])/2
B=A-temp1[0]
C=temp1[3]-B
if A-int(A)==0 and B-int(B)==0 and C-int(C)==0 and A>0 and B>0 and C>0:
    print(str(int(A))+" "+str(int(B))+" "+str(int(C)))
else:
    print("No")



