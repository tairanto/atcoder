#!/usr/bin/python3


N=int(input())
s=input()
n=0
plus=""
for i in s:
    if i=="(":
        n+=1
    else:
        if n:n-=1
        else:plus+="("
print(plus+s+")"*n)