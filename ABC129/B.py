#!/usr/bin/python3
n=int(input())
w=list(map(int,input().split()))
cs=[0]
for i in range(n):cs+=[cs[i]+w[i]]
ans=100000
for i in range(n):
    ans=min(ans,abs(cs[-1]-2*cs[i+1]))
print(ans)