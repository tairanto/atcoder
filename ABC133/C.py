#!/usr/bin/python3
L,R=map(int,input().split())
if R-L>=2018:
    print(0)
    exit()
l,r=L%2019,R%2019
if l>r:
    print(0)
else:
    ans=float("inf")
    for i in range(l,r+1):
        for j in range(i+1,r+1):
            ans=min(ans,i*j%2019)
    print(ans)