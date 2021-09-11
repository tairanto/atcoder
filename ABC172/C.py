#!/usr/bin/python3




N,M,K=map(int,input().split())
A,B=[*map(int,input().split())]+[float("inf")],[*map(int,input().split())]
time=0
for AN in range(N+1):
    if time+A[AN]<=K:
        time+=A[AN]
    else:
        break
ans=AN
for i in range(M):
    while AN>=0 and time+B[i]>K:
        time-=A[AN-1]
        AN-=1
    time+=B[i]
    ans=max(ans,i+1+AN)
    if AN<0:
        break
print(ans)