#!/usr/bin/python3

n=int(input())
s=[]
while n>0:
    if n%26==0:
        s.append(26)
        n=n//26-1
    else:
        s.append(n%26)
        n//=26
s.reverse()
print(*[chr(ord("a")+i-1) for i in s],sep="")