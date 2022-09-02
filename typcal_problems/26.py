#!/usr/bin/python3
import sys
sys.setrecursionlimit(10**9)
def dfs(x):
    now.add(x)
    ans[len(now)%2].add(x)
    for i in G[x]:
        if i in now:continue
        dfs(i)
    now.remove(x)

N=int(input())
G={i+1:[] for i in range(N)}
ans={0:set(),1:set()}
for i in range(N-1):
    a,b=map(int,input().split())
    G[a].append(b)
    G[b].append(a)

now=set()
dfs(1)
if len(ans[0])>len(ans[1]):
    print(*list(ans[0])[:N//2])
else:
    print(*list(ans[1])[:N//2])