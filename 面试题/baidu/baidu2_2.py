# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:20:41 2017

@author: mywow

question:
度度熊回家
【题目描述】一个数轴上共有N个点，第一个点的坐标是度度熊现在位置，第N-1个点是度度熊的家。现在他需要依次的从0号坐标走到N-1号坐标。但是除了0号坐标和N-1号坐标，他可以在其余的N-2个坐标中选出一个点，并直接将这个点忽略掉，问度度熊回家至少走多少距离？
输入描述:
输入一个正整数N, N <= 50。
接下来N个整数表示坐标，正数表示X轴的正方向，负数表示X轴的负方向。绝对值小于等于100
输出描述:
输出一个整数表示度度熊最少需要走的距离。
输入例子:
4
1 4 -1 3
输出例子:
4

solved way:穷举法
"""

num=int(input("请输入点的个数"))
located=input().split()
located=[int(i) for i in located]
ans=10000
for i in range(0,num):
    res=0
    last=located[0]
    for j in range(1,num-1):
        if i==j :continue
        res+=abs(located[j]-last)
        last=located[j]
    res+=abs(located[-1]-last)
    print(res)
    ans=min(ans,res)
print(ans)
    