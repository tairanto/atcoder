#!/usr/bin/python3
n,m=map(int,input().split())
ans=[[0,0] for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    ans[a][0]+=1
    ans[b][1]-=1
cnt=0
count=0
for i in range(1,n+1):
    cnt+=ans[i][0]
    if cnt==m:
        count+=1
    cnt+=ans[i][1]
print(count)