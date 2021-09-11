#!/usr/bin/python3
import bisect
def ok(mid):
    length=[0]
    for i in range(k):
        index=bisect.bisect(a,mid+length[-1])
        if a[index-1]==mid+length[-1]:
            length.append(a[index-1])
        elif index<n and mid+length[-1]<a[index]:
            length.append(a[index])
        else:
            return False
    if  l-length[-1]<mid:
        return False
    return True

n,l=map(int,input().split())
k=int(input())
a=list(map(int,input().split()))
top,bottom=l,0
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