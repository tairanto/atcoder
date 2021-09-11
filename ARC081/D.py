#!/usr/bin/python3

N=int(input())
s1=input()
s2=input()
now=0
ans=[6,3][s1[0]==s2[0]]
mod=10**9+7
while now<N-1:
    if s1[now]==s2[now]:
        now+=1
        ans=(ans*2)%mod
    else:
        if now+2<N and s1[now+2]!=s2[now+2]:
            ans=(ans*3)%mod
        now+=2
print(ans)



