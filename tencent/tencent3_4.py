# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:35:18 2017

@author: mywow
question:
gohash解码
【题目描述】geohash编码：geohash常用于将二维的经纬度转换为字符串，分为两步：第一步是经纬度的二
进制编码，第二步是base32转码。
此题考察纬度的二进制编码：算法对纬度[-90, 90]通过二分法进行无限逼近（取决于所需精度，本题精度为
6）。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右 。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右 。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右 。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右 。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右 。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右 。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右 。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右 。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右 。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右 。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右 。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右 。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右 。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右 。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右 。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右 。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右 。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右 。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右 。注意，本题进行二分法逼近过程中只采用向下取整来针对间值属于右
区间。算法举例如下： 区间。算法举例如下： 区间。算法举例如下： 区间。算法举例如下： 区间。算法举例如下：
针对纬度为80进行二进制编码过程：
1) 区间[-90, 90]进行二分为[-90, 0),[0, 90]，成为左右区间，可以确定80为右区间，标记为1；
2) 针对上一步的右区间[0, 90]进行二分为[0, 45),[45, 90]，可以确定80是右区间，标记为1；
3) 针对[45, 90]进行二分为[45, 67),[67,90],可以确定80为右区间，标记为1；
4) 针对[67,90]进行二分为[67, 78),[78,90]，可以确定80为右区间，标记为1；
5) 针对[78, 90]进行二分为[78, 84),[84, 90]，可以确定80为左区间，标记为0；
6) 针对[78, 84)进行二分为[78, 81), [81, 84)，可以确定80为左区间，标记为0；
已达精度要求，编码为111100。
样本输入：80
样本输出：111100
参考用例：
1、
输入：80
输出：111100
权重：1
2、
输入：0
输出：100000
21
3、
输入：-66
输出：001000
"""


num=0
def diguitest(left,right,target,count):
    
    temp=int((left+right)/2)
    if temp==target:
        print("count is "+str(count))
        return 0
    if target<temp:
        count+=1
        print(str(target)+"在区间的左侧，下次的区间缩小为：["+str(left)+","+str(temp-1)+"]")
        diguitest(left,temp-1,target,count)
    elif target>temp:
        count+=1
        print(str(target)+"在区间的右侧，下次的区间缩小为：["+str(temp+1)+","+str(right)+"]")
        diguitest(temp+1,right,target,count)
    if count>8:
        print("error")
        return -1
    

diguitest(-90,90,80,0)



        
    
