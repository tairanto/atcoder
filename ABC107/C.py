#!/usr/bin/python3
    

N,K=map(int,input().split())
n=[*map(int,input().split())]
n.sort()
ans=float("inf")
for i in range(N):
    if i+K-1<N:# and n[i]<= 0 <= n[i+K-1]:
        if n[i]*n[i+K-1]>0:
            ans=min(ans,max(abs(n[i]),abs(n[i+K-1])))
        else:
            ans=min(ans,min(abs(n[i]),n[i+K-1])+abs(n[i])+n[i+K-1])
print(ans)