#!/usr/bin/python3

n,m=map(int,input().split())
x=[list(map(int,input().split())) for i in range(m)]
x.sort()
num={}
for i in x:
    if not i[0] in num:
        num[i[0]]=[]
    num[i[0]].append(i[1])
print(num)
