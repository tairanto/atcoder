#!/usr/bin/python3

s=list(input())
s1,s2=s,[]
q=int(input())
r=0
for i in range(q):
    temp=input().split()
    if temp[0]=="1":
        r=(r+1)%2
    else:
        if temp[1]=="1":
            if r:
                s1.append(temp[2])
            else:
                s2.append(temp[2])
        else:
            if r:
                s2.append(temp[2])
            else:
                s1.append(temp[2])
if r:
    s1.reverse()
    print(*(s1+s2),sep="")
else:
    s2.reverse()
    print(*(s2+s1),sep="")