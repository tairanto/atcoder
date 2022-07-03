#!/usr/bin/python3

N=int(input())
s=[0 for i in range(2*10**5+10)]
for i in range(N):
    L,R=map(int,input().split())
    s[L]+=1
    s[R]-=1

now=0
ans=[]
for n,i in enumerate(s):
    if i:
        if now==0:
            ans.append([n])
        else:
            if now+i==0:
                ans[-1].append(n)
        now+=i
for i in ans:
    print(*i)