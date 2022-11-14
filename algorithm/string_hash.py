#!/usr/bin/python3

def hash(x,y):
    num=(dp[y]-dp[x-1]*pow(26,y-x+1,mod))%mod
    return num

N,Q=map(int,input().split())
S=input()
dp=[0]
mod=2147483647
for i in S:
    dp.append((dp[-1]*26+ord(i)-97)%mod)

for i in range(Q):
    a,b,c,d=map(int,input().split())
    AB=hash(a,b)
    CD=hash(c,d)
    print("Yes" if AB==CD else "No")