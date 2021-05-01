#!/usr/bin/python3
n,x=map(int,input().split())
l=list(map(int,input().split()))
cnt,ans=1,0
for i in l:
    ans+=i
    if ans<=x:
        cnt+=1
print(cnt)