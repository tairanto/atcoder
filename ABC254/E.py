#!/usr/bin/python3


def dfs(x,dep):
    touch.add(x)
    if dep>0:
        for to in edge[x]:
            dfs(to,dep-1)

def solve():
    global touch
    x,k=map(int,input().split())
    touch=set()
    x-=1
    dfs(x,k)
    print(sum(touch)+len(touch))

N,M=map(int,input().split())
edge=[[] for i in range(N)]

for i in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    edge[a].append(b)
    edge[b].append(a)

Q=int(input())

for i in range(Q):
    solve()