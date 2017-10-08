# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:45:22 2017

@author: mywow
question:
跳石板
【题目描述】小易来到了一条石板路前，每块石板上从1挨着编号为：1、2、3.......
这条石板路要根据特殊的规则才能前进：对于小易当前所在的编号为K的石板，小易单次只能往前跳K的一个约数(不含1和K)步，
即跳到K+X(X为K的一个非1和本身的约数)的位置。 小易当前处在编号为N的石
板，他想跳到编号恰好为M的石板去，小易想知道最少需要跳跃几次可以到达。
例如：
N = 4，M = 24：
4->6->8->12->18->24
于是小易最少需要跳跃5次，就可以从4号石板跳到24号石板
输入描述:
输入为一行，有两个整数N，M，以空格隔开。
(4 ≤ N ≤ 100000)
(N ≤ M ≤ 100000)
28
输出描述:
输出小易最少需要跳跃的步数,如果不能到达输出-1
输入例子:
4 24
输出例子:
5
"""
inputs=input().split()
inputs=[int(i) for i in inputs]
n=inputs[0]
m=inputs[1]
remain=-1
loop=m-n+1
step=0
flag=0
for i in range(loop):
    print("当前的位置为:"+str(n))
    remain=m-n
    print("当前剩余距离："+str(remain))
    if remain==0:
        print("跳完了，一共跳了"+str(step)+"次")
        flag=1
        break;
    for j in range(int(n/2)+1,1,-1):
        if n%j==0 and j<=remain:
            print("这次可跳"+str(j)+"步")
            n+=j
            print("新的位置为:"+str(n))
            step+=1
            print("已经跳了"+str(step)+"步")
            break;
        
if flag==0:
   print(-1)
            
        
    
