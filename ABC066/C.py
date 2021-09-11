#!/usr/bin/python3

n=int(input())
r=0
s1,s2=[],[]
for i in list(map(int,input().split())):
    if r:
        s2.append(i)
    else:
        s1.append(i)
    r=(r+1)%2
if r:
    s1.reverse()
    print(*(s1+s2))
else:
    s2.reverse()
    print(*(s2+s1))
