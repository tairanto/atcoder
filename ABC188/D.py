#!/usr/bin/python3

N,C=map(int,input().split())
s=[]
for i in range(N):
    a,b,c=map(int,input().split())
    s.append([a-1,c])
    s.append([b,-c])
s.sort()
ans=0
money=0
now=0
for i in s:
    if now!=i[0]:
        ans+=min(C,money)*(i[0]-now)
        now=i[0]
    money+=i[1]
print(ans)