#!/usr/bin/python3


N,A,B=map(int,input().split())
X=[*map(int,input().split())]
ans=0
for i in range(N-1):
    ans+=min((X[i+1]-X[i])*A,B)
print(ans)