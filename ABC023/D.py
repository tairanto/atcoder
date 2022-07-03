#!/usr/bin/python3

def ok(x):
    ans=sorted([(x-i[0])/i[1] for i in hs])
    for n,i in enumerate(ans):
        if i<n:return False
    return True

N=int(input())
hs=[[*map(int,input().split())] for i in range(N)]
top,bottom=10**18,0
while top-bottom>1:
    mid=(top+bottom)//2
    if ok(mid):
        top=mid
    else:
        bottom=mid
print(max(top,bottom))