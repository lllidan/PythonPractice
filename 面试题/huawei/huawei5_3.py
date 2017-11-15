# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:55:49 2017

@author: mywow
question:
计算字符串中最后一个单词的长度
【题目描述】给定一个字符串s由大小写字母和空格组成的字符串，返回字符串的最后一个单词的长度；单词不包含空格；如果最后一个单词不存在，返回0；
牛客网——国内最大的 IT 笔试面试题库
34
例如"Hello World",返回5
输入说明：
输入1行字符串
输出说明：
输出字符串最后一个单词的长度
样例输入：
I am Lisa
样例输出：
4
"""
strings = input()

words = strings.split(' ')

word = words[-1]

length = 0

for i in word:
    length =length + 1
    
print(length)
