#!/usr/bin/python3
import sys
sys.setrecursionlimit(10**9)

def dfs(now):
  seen.add(now)
  if ans[0]<len(seen):
    ans[0],ans[1]=len(seen),now
  for i in G[now]:
    if i in seen:continue
    dfs(i)
  seen.remove(now)

N=int(input())
G={i+1:[] for i in range(N)}
for i in range(N-1):
  a,b=map(int,input().split())
  G[a].append(b)
  G[b].append(a)
seen=set()
ans=[0,1]
dfs(1)
dfs(ans[1])
print(ans[0])