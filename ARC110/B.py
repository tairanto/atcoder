#!/usr/bin/python3

import math
n,t=int(input()),list(input())
temp=["1","1","0"]*(n//3+2)
for i in range(3):
    if temp[i:i+n]==t:
        if n==1:
            if t==["1"]:print(2*10**10)
            else:print(10**10)
        elif n==2:
            if t==["1","1"] or t==["1","0"]:print(10**10)
            elif t==["0","1"]:print(10**10-1)
            else:print(0)
        else:
            print(10**10-math.ceil((n-(3-i))/3))
        exit()
print(0)