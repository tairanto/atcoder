#!/usr/bin/python3


mod = 998244353
H, W = map(int, input().split())
S=[list(input()) for i in range(H)]

ans=1
for i in range(H+W+1):
    temp=set()
    for j in range(H):
        k=i-j
        if 0<=k<W:
            temp.add(S[j][k])
    if "B" in temp and "R" in temp:
        ans*=0
    elif "." in temp and len(temp)==1:
        ans=(ans*2)%mod
print(ans)