#!/usr/bin/python3
import sys
sys.setrecursionlimit(10**9)
def dfs(i):
    seen[i-1]=1
    c[colar[i-1]]+=1
    for j in graph[i]:
        if seen[j-1]:continue
        dfs(j)
        if c[colar[j-1]]>0:ans[j-1]=0
    c[colar[i-1]]-=1

n=int(input())
colar=list(map(int,input().split()))
graph={i+1:[] for i in range(n)}
for i in range(n-1):
    temp=list(map(int,input().split()))
    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])
ans=[1 for i in range(n)]
seen=[0 for i in range(n)]
c=[0 for i in range(10**5+1)]
dfs(1)
for i in range(n):
    if ans[i]:print(i+1)