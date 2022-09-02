#!/usr/bin/python3

from re import X


N=int(input())
grid=[list(input()) for i in range(N)]
X=[-1,-1,-1,0,0,1,1,1]
Y=[-1,0,1,-1,1,-1,0,1]
ans=0
for i in range(N):
    for j in range(N):
        for d in range(8):
            temp=""
            for k in range(N):
                temp+=grid[(i+k*X[d])%N][(j+k*Y[d])%N]
            ans=max(ans,int(temp))
print(ans)