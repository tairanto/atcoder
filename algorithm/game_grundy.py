#!/usr/bin/python3

N,X,Y=map(int,input().split())
dp=[0]*(100050)
for i in range(100050):
    bit=[1,1,1]#2の場合だから0,1,2のmex
    if i>=X:
        bit[dp[i-X]]=0
    if i>=Y:
        bit[dp[i-Y]]=0
    if bit[0]:
        dp[i]=0
    elif bit[1]:
        dp[i]=1
    else:
        dp[i]=2
print("First" if dp[N] else "Second")