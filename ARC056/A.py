#!/usr/bin/python3

a,b,k,l=map(int,input().split())
if a<=b/l:
    print(a*k)
else:
    total=(k//l)*b
    k-=(k//l)*l
    if a*k<=b:
        print(total+a*k)
    else:
        print(total+b)