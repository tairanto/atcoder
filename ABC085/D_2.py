#!/usr/bin/python3


N,H=map(int,input().split())
A,B=[],[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
M=max(A)
B.sort()
ans=0
while H>0:
    if B and B[-1]>=M:
        H-=B.pop(-1)
        ans+=1
    else:
        ans+=H//M+(H%M>0)
        break
print(ans)