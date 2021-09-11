#!/usr/bin/python3


N=int(input())
A=sorted([*map(int,input().split())])
c=[0]
for i in A:
    c.append(i+c[-1])
ans=1
for i in range(N-1):
    if c[-2-i]*2>=A[-1-i]:
        ans+=1
    else:
        break
print(ans)