# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 17:46:13 2017

@author: mywow
question:有趣的排序
【题目描述】度度熊有一个N个数的数组，他想将数组从小到大 排好序，但是萌萌的度度熊只会下面这个操作：
任取数组中的一个数然后将它放置在数组的最后一个位置。
问最少操作多少次可以使得数组从小到大有序？
输入描述:
首先输入一个正整数N，接下来的一行输入N个整数。(N <= 50, 每个数的绝对值小于等于1000)
输出描述:
输出一个整数表示最少的操作次数。
输入例子:
4
19 7 8 25
输出例子:
2
"""

num=int(input("please input the numbers of number"))
numbers=input().split()
numbers=[int(i) for i in numbers]
sortednumbers=[]
for i in numbers:
    sortednumbers.append(i)
list.sort(sortednumbers)
for i in numbers:
    print(i,end=" ")
print()
for i in sortednumbers:
    print(i,end=" ")
print()
q=-1
n=len(numbers)-1
for i in range(0,n+1):
    if numbers[i]==sortednumbers[q+1]:
        q+=1
        if q==n :
            break
print(n-q)