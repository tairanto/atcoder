#!/usr/bin/python3


n,m=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
cd=[list(map(int,input().split())) for i in range(m)]
for i in ab:
    cnt=float("inf")
    for j in range(m):
        temp=abs(i[0]-cd[j][0])+abs(i[1]-cd[j][1])
        if cnt>temp:
            cnt=temp
            ans=j+1
    print(ans)