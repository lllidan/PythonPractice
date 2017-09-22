# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:43:48 2017

@author: mywow
question:
数字翻转
【题目描述】对于一个整数X，定义操作rev(X)为将X按数位翻转过来，并且去除掉前导0。例如:
如果 X = 123，则rev(X) = 321;
如果 X = 100，则rev(X) = 1.
现在给出整数x和y,要求rev(rev(x) + rev(y))为多少？
输入描述:
输入为一行，x、y(1 ≤ x、y ≤ 1000)，以空格隔开。
输出描述:
输出rev(rev(x) + rev(y))的值
输入例子:
123 100
输出例子:
223
"""
nums=input().split()
numx=[0 for i in range(len(nums[0]))]
numy=[0 for i in range(len(nums[1]))]

for i in range(len(nums[0])):
    numx[len(nums[0])-i-1]=nums[0][i]
for i in range(len(nums[1])):
    numy[len(nums[1])-i-1]=nums[1][i]
    
sumx=0
sumy=0
for i in range(len(numx)):
    sumx+=int(numx[i])*10**(len(numx)-1-i)
for i in range(len(numy)):
    sumy+=int(numy[i])*10**(len(numy)-1-i)
count=str(sumx+sumy)
for i in range(len(count)):
    print(count[len(count)-1-i],end='')

