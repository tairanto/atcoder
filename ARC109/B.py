#!/usr/bin/python3
def ok(mid):
    if mid*(mid+1)//2<=n+1:
        return True
    else:
        return False

n=int(input())
top=n+1
bottom=0
while top-bottom>1:
    mid=(top+bottom)//2
    if ok(mid):bottom=mid
    else:top=mid
if ok(top):
    print(n+1-top)
else:
    print(n+1-bottom)