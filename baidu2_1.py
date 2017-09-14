# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 22:32:01 2017

@author: mywow

1、 买帽子
【题目描述】度度熊想去商场买一顶帽子，商场里有N顶帽子，有些帽子的价格可能相同。度度熊想买一顶价格第三便宜的帽子，问第三便宜的帽子价格是多少？
输入描述:
首先输入一个正整数N（N <= 50），接下来输入N个数表示每顶帽子的价格（价格均是正整数，且小于等于
1000）
输出描述:
如果存在第三便宜的帽子，请输出这个价格是多少，否则输出-1
输入例子:
10
10 10 10 10 20 20 30 30 40 40
输出例子:
30
分析：因为Python可以自主的遍历数组，所以输入的帽子数量没什么用
"""

N=int(input("输入帽子数"))
prices=input().split();
prices=[int(i) for i in prices]
list.sort(prices)
sortprices=set(prices)
prices=list(sortprices)
list.sort(prices)
if len(prices)>2:
    print(prices[2])
else:
    print(-1)

