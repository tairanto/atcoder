#!/usr/bin/python3

N=int(input())
waza=[[*map(int,input().split())] for i in range(N)]
need=set(waza[N-1][2:])
ans=waza[N-1][0]
for i in range(N-2,-1,-1):
    if i+1 in need:
        ans+=waza[i][0]
        need|=set(waza[i][2:])
print(ans)