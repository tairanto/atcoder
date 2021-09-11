#!/usr/bin/python3

n,m,k=map(int,input().split())
A=[list(map(int,input().split())) for i in range(n)]
ans=float("inf")
for i in range(1,1<<n):
    temp=[0 for i in range(m+1)]
    for j in range(n):
        if (i>>j)%2==1:
            for l in range(m+1):
                temp[l]+=A[j][l]
    if min(temp[1:])>=k:
        ans=min(temp[0],ans)
if ans==float("inf"):
    print(-1)
else:
    print(ans)