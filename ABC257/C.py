#!/usr/bin/python3


import bisect

N=int(input())
S=[*map(int,list(input()))]
W=[*map(int,input().split())]+[1,10**9]
child,adult=[],[]
for i in range(N):
    if S[i]:adult.append(W[i])
    else:child.append(W[i])
adult.sort()
child.sort()
ans=0
for i in W:
    ans=max(ans,len(adult)-bisect.bisect_left(adult,i)+bisect.bisect_left(child,i))
print(ans)