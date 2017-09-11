# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 19:04:02 2017

@author: mywow
2、集合
【题目描述】给你两个集合，要求{A}+{B}。
注：同一个集合中不会有两个相同的元素。
输入：
多组（不超过5组）数据。
每组输入数据分为三行，第一行有两个数字n，m（$0<n,m\leq10000$），分别表示集合A和集合B的元素个
数。后两行分别表述集合A和集合B。每个元素为不超出int范围的整数，每个元素之间有一个空格隔开。
输出：
针对每组数据输出一行数据，表示合并后的集合，要求从小到大输出，每个元素之间有一个空格隔开。
样例输入
1 2
1
2 3
1 2
1
1 2
样例输出
1 2 3
牛客网——国内最大的 IT 笔试面试题库
3
1 2
"""

countA,countB= map(int,input().split())

sets=set()
setA=set()
setB=set()
setA=map(int,input().split())
for i in setA:
    sets.add(i)
setB=map(int,input().split())
for i in setB:
    sets.add(i)
for i in sets:
    print(str(i), end=' ')