#!/usr/bin/python3


N=int(input())
S=input()
a={chr(i):0 for i in range(97,97+26)}
for i in range(N):
    a[S[i]]+=1
ans=1
for i in a:
    ans*=(a[i]+1)
print(ans%(10**9+7)-1)