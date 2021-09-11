#!/usr/bin/python3

N=int(input())
T=sorted([int(input()) for i in range(N)])
mod=10**9+7
k=[1]
for i in range(1,10**4+1):
    k.append((k[-1]*i)%mod)
ans=[0]
num={}
for i in T:
    if not i in num:
        num[i]=0
    num[i]+=1 
    ans.append(i+ans[-1])
p=1
for i in num:
    p*=k[num[i]]
print(sum(ans),p%mod,sep="\n")