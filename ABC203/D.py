#!/usr/bin/python3
n,k=map(int,input().split())
A=[list(map(int,input().split())) for i in range(n)]
ans=float("inf")
for i in range(n-k+1):
    temp=[]
    for j in range(n-k+1):
        if j==0 and i==0:
            for m in range(k):
                for l in range(k):
                    temp.append(A[i+l][j+m])
        else:
            for l in range(k):
                temp.append(A[i+l][j+m])
        t=sorted(temp[k*j:])
        ans=min(ans,t[(k*k//2+1)*(-1)])
print(ans)
