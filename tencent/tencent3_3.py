# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:32:58 2017

@author: mywow
question:
3、质数对
【题目描述】给定一个正整数，编写程序计算有多少对质数的和等于输入的这个正整数，并输出结果。输入值小于1000。如，输入为10，程序应该输出结果为2。（共有两对质数的和为10，分别为（5,5）（3.7））
牛客网——国内最大的 IT 笔试面试题库
19
参考用例：
1、
输入：3
输出：0
2、
输入：50
输出：4
3、
输入：100
输出：6
"""

n=int(input("input a number:"))
flag=1
prime=[]
for i in range(2,n):
    flag=1
    for j in range(2,n//2):
        if(i==j):
            continue
        if (i%j==0):
            flag=0
            break
    if(flag==1):
        prime.append(i)
count=0
for i in range(0,len(prime)):
    for j in range(i,len(prime)):
        if prime[i]+prime[j]==n:
           count+=1
print(count)

