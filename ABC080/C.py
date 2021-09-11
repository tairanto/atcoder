#!/usr/bin/python3

N=int(input())
F=[[*map(int,input().split())] for _ in range(N)]
P=[[*map(int,input().split())] for _ in range(N)]
ans=-float("inf")
for i in range(1,1<<10):
    n=[0 for _ in range(N)]
    for j in range(10):
        if (i>>j)%2:
            for k in range(N):
                if F[k][j]:
                    n[k]+=1
    ans=max(sum([P[j][n[j]] for j in range(N)]),ans)
print(ans)