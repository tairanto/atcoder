#!/usr/bin/python3
def ok(mid):
    n=len(str(mid))
    if mid*a+n*b<=x:
        return True
    else:
        return False

a,b,x=map(int,input().split())
top,bottom=10**9,0
while top-bottom>1:
    mid=(top+bottom)//2
    if ok(mid):
        bottom=mid
    else:
        top=mid
if ok(top):
    print(top)
else:
    print(bottom)