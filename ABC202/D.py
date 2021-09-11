#!/usr/bin/python3
from math import factorial
def com(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))
ans=""
a,b,n=map(int,input().split())
total=a+b
for i in range(1,total+1):
    if a==0:
        ans+="b"
        continue
    elif b==0:
        ans+="a"
        continue
    if i==total:
        if a:ans+="a"
        else:ans+="b"
    temp=com(total-i,b)
    if n<=temp:
        ans+="a"
        a-=1
    else:
        ans+="b"
        n-=temp
        b-=1
print(ans)