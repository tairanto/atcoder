#!/usr/bin/python3

n,m=map(int,input().split())
num={}
for i in list(map(int,input().split())):
    if not i in num:
        num[i]=0
    num[i]+=1
M=max(num.values())
ans=[i for i in num if num[i]==M]
if len(ans)==1 and M>n//2:
    print(ans[0])
else:
    print("?")