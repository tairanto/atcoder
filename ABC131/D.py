#!/usr/bin/python3
n=int(input())
x=[list(map(int,input().split())) for i in range(n)]
x.sort(key=lambda x:x[1])
ans=0
for i in x:
    ans+=i[0]
    if ans>i[1]:
        print("No")
        exit()
print("Yes")