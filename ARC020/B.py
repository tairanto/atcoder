#!/usr/bin/python3

N,C=map(int,input().split())
a=[int(input()) for i in range(N)]
f,s={i:0 for i in range(1,11)},{i:0 for i in range(1,11)}
for i in range(N):
    if i%2:
        s[a[i]]+=1
    else:
        f[a[i]]+=1
ans=float("inf")
for i in range(1,11):
    for j in range(1,11):
        if i==j:continue
        ans=min(ans,N-s[i]-f[j])
print(ans*C)