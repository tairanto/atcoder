#!/usr/bin/python3

import sys
sys.setrecursionlimit(10**9)
def dfs(v,ptr,Now):
    seen[v-1]=1
    count[0]+=1
    if ans[Now][v][0]>ptr:
        ans[Now][v][0]= ptr
        ans[Now][v][1]= count[0]
    for i in G[v]:
        if seen[i[0]-1]:continue
        ptr+=i[1]
        ptr=dfs(i[0], ptr,Now)
        ptr-=i[1]
        seen[i[0]-1]=0
    count[0]-=1
    return ptr
diff=[0]
count=[0]
N,M=map(int,input().split())
ans={i+1:{j+1:[float("inf"),float("inf")] for j in range(N)} for i in range(N)}
G={i+1:[] for i in range(N)}
for i in range(M):
    A,B,C=map(int,input().split())
    G[A].append([B,C])
    
for i in range(1,N+1):
    seen=[0 for i in range(N)]
    seen[i-1]=1
    for j in G[i]:
        if seen[j[0]-1]:continue
        ptr=j[1]
        ptr=dfs(j[0],ptr,i)
total=0
print(ans)
for i in range(1,N+1):
    for j in range(1,N+1):
        if ans[i][j][0]==float("inf"):continue
        total+=ans[i][j][0]*(N-ans[i][j][1]+1)
print(total)