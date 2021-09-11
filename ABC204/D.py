#!/usr/bin/python3
n=int(input())
t=list(map(int,input().split()))
temp=set()
temp.add(0)
for i in t:
    for j in list(temp):
        temp.add(j+i)
ans=float("inf")
total=sum(t)
for i in temp:
    ans=min(ans,max(total-i,i))
print(ans)