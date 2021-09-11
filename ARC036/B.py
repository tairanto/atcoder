#!/usr/bin/python3

N=int(input())
H=[int(input()) for _ in range(N)]
right,left=[0],[0]
r,l=0,0
for i in range(N):
    if r<H[i]:
        right.append(right[-1]+1)
    else:
        right.append(1)
    if l<H[-1-i]:
        left.append(left[-1]+1)
    else:
        left.append(1)
    r,l=H[i],H[-1-i]
ans=0
for i in range(N):
    ans=max(ans,right[1+i]+left[-1-i]-1)
print(ans)