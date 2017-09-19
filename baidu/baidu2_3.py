# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:56:25 2017

@author: mywow
question:寻找三角形
【题目描述】三维空间中有N个点，每个点可能是三种颜色的其中之一，三种颜色分别是红绿蓝，分别用'R',
'G', 'B'表示。
现在要找出三个点，并组成一个三角形，使得这个三角形的面积最大。
但是三角形必须满足：三个点的颜色要么全部相同，要么全部不同。
输入描述:
首先输入一个正整数N三维坐标系内的点的个数.(N <= 50)
接下来N行，每一行输入 c x y z，c为'R', 'G', 'B' 的其中一个。x，y，z是该点的坐标。(坐标均是0到
999之间的整数)
输出描述:
牛客网——国内最大的 IT 笔试面试题库
11
输出一个数表示最大的三角形面积，保留5位小数。
输入例子:
5
R 0 0 0
R 0 4 0
R 0 0 3
G 92 14 7
G 12 16 8
输出例子:
6.00000
"""

from math import sqrt
class point(object):
    def __init__(self,col,X,Y,Z):
        self.col=col
        self.X=int(X)
        self.Y=int(Y)
        self.Z=int(Z)
def areaCal(A,B,C):
    AB=sqrt((B.X-A.X)**2+(B.Y-A.Y)**2+(B.Z-A.Z)**2)
    AC=sqrt((C.X-A.X)**2+(C.Y-A.Y)**2+(C.Z-A.Z)**2)
    BC=sqrt((B.X-C.X)**2+(B.Y-C.Y)**2+(B.Z-C.Z)**2)
    p=(AB+AC+BC)/2
    area=sqrt(p*(p-AB)*(p-BC)*(p-AC))
    return area
    
if __name__=='__main__':
    num=int(input("输入点的个数"))
    print(num)
    points=[]
    area=0
    for i in range(0,num):
       temp=input().split()
       points.append(point(temp[0],temp[1],temp[2],temp[3]))
    for i in range(0,num-2):
        for j in range(i+1,num-1):
            for k in range(j+1,num):
                if ((points[i].col==points[j].col)and(points[i].col==points[k].col))or((points[i].col!=points[j].col)and(points[j].col!=points[k].col) and (points[i].col!=points[k].col)):
                    temparea=areaCal(points[i],points[j],points[k])
                    if temparea>area:
                        area=temparea
    print(area)
