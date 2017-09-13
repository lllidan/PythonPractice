# -*- coding: utf-8 -*-
"""
3、通过考试
【题目描述】小明同学要参加一场考试，考试一共有n道题目，小明必须做对至少60%的题目才能通过考试。
考试结束后，小明估算出每题做对的概率，p1,p2,...,pn。你能帮他算出他通过考试的概率吗？
输入
输入第一行一个数n（1<=n<=100），表示题目的个数。第二行n个整数，p1,p2,...,pn。表示小明有pi%的概
率做对第i题。（0<=pi<=100）
输出
小明通过考试的概率，最后结果四舍五入，保留小数点后五位。
样例输入
4
50 50 50 50
样例输出
0.31250
"""
num=int(input("请输入考试的题目数"));'输入题目数'
a = []
a.append(0)
for i in range(1,num+1):
    a.append(int(input("请依次输入每道题做对的概率")));
dp = [[0 for col in range(105)] for row in range(105)]
dp[0][0]=1
for i in range(1,num+1):
    dp[i][0]=dp[i-1][0] * (100.0-a[i])/100
    print(dp[i][0])
    for j in range(1,i+1):
        dp[i][j]=dp[i-1][j] * (100.0-a[i])/100 +dp[i-1][j-1]*1.0*a[i]/100

for i in range(1,num+1):
    for j in range(0,i+1):
        print("dp["+str(i)+"]["+str(j)+"]:"+str(dp[i][j]),end=" ")
    print()
begin =int((3*num+4)/5)
print("至少要做对"+str(begin)+"道题")
ans=0.0
for i in range(begin,num+1):
    ans+=dp[num][i]
print("你通过考试的概率为:"+str(ans))










