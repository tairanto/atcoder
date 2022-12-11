#!/usr/bin/python3

import sys
sys.setrecursionlimit(10**9)
def fdfs(x):
    come[x]=1
    for i in g_f[x]:
        if come[i]:continue
        fdfs(i)
    back.append(x)

def rdfs(x):
    come[x]=1
    ans[-1].append(x)
    for to in g_r[x]:
        if come[to]:continue
        rdfs(to)


N,M=map(int,input().split())
g_f=[[] for i in range(N+1)]
g_r=[[] for i in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    g_f[a].append(b)
    g_r[b].append(a)

come=[0]*(N+1)
back=[]
for i in range(1,N+1):
    if come[i]:continue
    fdfs(i)

come=[0]*(N+1)
ans=[]
for i in back[::-1]:
    if come[i]:continue
    ans.append([])
    rdfs(i)

total=0
for i in ans:
    n=len(i)
    total+=n*(n-1)//2
print(total)