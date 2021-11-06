#!/usr/bin/python3

def half(c,num):
    bottom=0
    top=num
    while top-bottom>1:
        if dp[(top+bottom)//2]>c:top=(top+bottom)//2
        else:bottom=(top+bottom)//2
    if dp[bottom]>c:
        dp[bottom]=c
    else:
        dp[top]=c

N=int(input())
dp=[float("inf") for i in range(N+1)]
dp[0]*=-1
num=0
for _ in range(N):
    c=int(input())
    if dp[num]<c:
        dp[num+1]=c
        num+=1
    else:
        half(c,num)
print(N-num)