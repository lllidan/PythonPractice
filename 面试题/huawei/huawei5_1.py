# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:52:51 2017

@author: mywow
question:
计算海滩上桃子有多少个
【题目描述】海滩上有一堆桃子，m只猴子来分。第一只猴子把这堆桃子平均分为m份，多了一个，
这只猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下的桃子又平均分成m份，又多了一个，
它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只、第m只猴子都是这样做的，
问海滩上原来最少有多少个桃子？
输入：
输入猴子个数m（3<=m<=9）
输出：
原来最少有多少个桃子
样例输入：
3
"""

monkey = int(input("请输入猴子的数量"))

peach = 1

for i in range(monkey):
    peach = peach * monkey
    
print(peach - monkey +1)