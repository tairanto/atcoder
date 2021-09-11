#!/usr/bin/python3

q,h,s,d=map(int,input().split())
ice=[[q*8,0.25,q],[h*4,0.5,h],[s*2,1,s],[d,2,d]]
ice.sort()

n=int(input())
ans=0
for i in range(4):
    ans+=int((n//ice[i][1])*ice[i][2])
    n-=int((n//ice[i][1])*ice[i][1])
print(ans)