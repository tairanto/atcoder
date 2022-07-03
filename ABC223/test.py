#!/usr/bin/python3

N,M=map(int,input().split())
ans=[[] for i in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    ans[b].append(a)
print(ans)
1234