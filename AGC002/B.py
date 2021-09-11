#!/usr/bin/python3

N,M=map(int,input().split())
ball=[1 for i in range(N)]
ans=[0 for i in range(N)]
ans[0]=1
for i in range(M):
    x,y=map(int,input().split())
    x,y=x-1,y-1
    if ans[x]:
        ans[x]=ball[x]>1
        ans[y]=1
    ball[x]-=1
    ball[y]+=1
print(sum(ans))
        