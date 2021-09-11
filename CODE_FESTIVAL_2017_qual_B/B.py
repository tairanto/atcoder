#!/usr/bin/python3


n=int(input())
d={}
for i in list(map(int,input().split())):
    if not i in d:
        d[i]=0
    d[i]+=1
m=int(input())
for i in list(map(int,input().split())):
    if not i in d or d[i]==0:
        print("NO")
        exit()
    else:
        d[i]-=1
print("YES")