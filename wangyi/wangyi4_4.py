# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:44:28 2017

@author: mywow
question:
暗黑的字符串
【题目描述】一个只包含'A'、'B'和'C'的字符串，如果存在某一段长度为3的连续子串中恰好'A'、'B'和'C
各有一个，那么这个字符串就是纯净的，否则这个字符串就是暗黑的。例如：
BAACAACCBAAA 连续子串"CBA"中包含了'A','B','C'各一个，所以是纯净的字符串
AABBCCAABB 不存在一个长度为3的连续子串包含'A','B','C',所以是暗黑的字符串
你的任务就是计算出长度为n的字符串(只包含'A'、'B'和'C')，有多少个是暗黑的字符串。
输入描述:
输入一个整数n，表示字符串长度(1 ≤ n ≤ 30)
输出描述:
输出一个整数表示有多少个暗黑字符串
输入例子:
2
3
输出例子:
9
21
"""

dp1=[0 for col in range(105)]
dp2=[0 for col in range(105)]
n=int(input())
dp1[1]=0
dp1[2]=3
dp2[0]=1
dp2[1]=3
dp2[2]=6
for i in range(3,n+1):
    dp1[i] = dp1[i - 1] + dp2[i - 1]
    dp2[i] = dp1[i - 1] * 2 + dp2[i - 1];
print(dp1[n]+dp2[n])
