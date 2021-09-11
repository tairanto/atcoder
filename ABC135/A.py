#!/usr/bin/python3
a,b=map(int,input().split())
if (a-b)%2:
    print("IMPOSSIBLE")
else:
    print(abs(a-b)//2+min(a,b))