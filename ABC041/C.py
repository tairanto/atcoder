#!/usr/bin/python3

n=int(input())
ans=[]
for x,i in enumerate(list(map(int,input().split()))):
    ans.append([i,x])
ans.sort(reverse=True)
for i in ans:
    print(i[1]+1)