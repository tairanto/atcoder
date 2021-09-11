#!/usr/bin/python3

import sys
sys.setrecursionlimit(10**9)

def dislike(x):
    for i in temp:
        if x>n and i>n:continue
        if x<=n and i<=n:continue
        if not x in Graph[i]:
            return True
    return False

def dfs(v):
    temp.add(v)
    seen[v-1] = 1
    for i in Graph[v]:
        if seen[i-1]:continue
        if dislike(i):continue
        dfs(i)
    ans[0]=max(ans[0],sum(seen))


n,m,k=map(int,input().split())
Graph={i+1:set() for i in range(n+m)}
for i in range(k):
    a,b=map(int,input().split())
    Graph[a].add(b+n)
    Graph[b+n].add(a)
ans=[0]
for i in range(1,n+m+1):
    seen=[0 for i in range(n+m)]
    temp=set()
    dfs(i)
print(max(n,m,ans[0]))