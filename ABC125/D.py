#!/usr/bin/python3
n=int(input())
x=list(map(int,input().split()))
m=10**9+1
cnt=0
for i in x:
    if i==0:
        cnt=0
        m=10**9+1
    else:
        m=min(m,abs(i))
        if i<0:
            cnt+=1
if cnt%2:
    print(sum([abs(i) for i in x])-2*m)
else:
    print(sum([abs(i) for i in x]))