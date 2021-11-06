#!/usr/bin/python3


def dp(x,a,b,ab,bb):
    temp=[0 for i in range(3000+1)]
    S=0
    for i in range(3000+1):
        if ab<=i<=bb:
            S+=x[i]
        if a<=i<=b:
            temp[i]=S
        elif i>b:
            break
        else:
            temp[i]=x[i]
    return temp
            
N=int(input())
A,B=[*map(int,input().split())],[*map(int,input().split())]
ans=1
mod=998244353
ans=[0 for i in range(3000+1)]
for i in range(N):
    if i==0:
        for j in range(A[i],B[i]+1):
            ans[j]+=1
        continue
    ans=dp(ans,A[i],B[i],A[i-1],B[i-1])
print(sum(ans[A[-1]:B[-1]+1])%mod)