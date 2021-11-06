#!/usr/bin/python3

N,K=map(int,input().split())
ans=0
for i in range(K+1,N+1):
    ans+=(N//i)*(i-K)
    if (N//i)*i+K<=N:
        ans+=N-(N//i)*i-K+1-(K==0)
print(ans)