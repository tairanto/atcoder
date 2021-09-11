#!/usr/bin/python3


N,K=map(int,input().split())
a=[*map(int,input().split())]
ans=0
for i in range(N):
    if N//2+N%2==i:break
    ans+=min(i+1,N-K+1,K)*(a[i]+a[-1-i]-[0,a[i]][i==N//2])
print(ans)