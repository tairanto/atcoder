#!/usr/bin/python3


N,K=map(int,input().split())
A=sorted([*map(int,input().split())]+[0])
count=1
ans=0
for i in range(N,-1,-1):
    if not A[i]:break
    diff=(A[i]-A[i-1])*count
    if diff<K:
        K-=diff
        ans+=(A[i]*(A[i]+1)//2-A[i-1]*(A[i-1]+1)//2)*count
        count+=1
    else:
        n=K//count
        ans+=(A[i]*(A[i]+1)//2-(A[i]-n)*(A[i]-n+1)//2)*count
        amari=K%count
        ans+=(A[i]-n)*amari
        break
print(ans)