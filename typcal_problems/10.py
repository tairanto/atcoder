#!/usr/bin/python3

one,two=[0],[0]
for _ in range(int(input())):
    c,p=map(int,input().split())
    one.append(one[-1]+p*(c==1))
    two.append(two[-1]+p*(c!=1))
for _ in range(int(input())):
    l,r=map(int,input().split())
    print(one[r]-one[l-1],two[r]-two[l-1])