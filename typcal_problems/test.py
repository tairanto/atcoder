#!/usr/bin/python3


def cal(t,bit,x):
    if t==1:
        bit&=x
    elif t==2:
        bit|=x
    else:
        bit^=x
    return bit

N,C=map(int,input().split())
ta=[[*map(int,input().split())] for i in range(N)]
for i in range(N):
    t,x=ta[i]
    if i==0:
        bit=x
    else:
        bit=cal(t,bit,x)
    print("a",C,bit)
    C=cal(ta[0][0],C,bit)
    print(C)