#!/usr/bin/python3

K,T=map(int,input().split())
a={x+1:i for x,i in enumerate([*map(int,input().split())])}

while len(a)>1:
    m,M=[float("inf"),0],[0,0]
    for i in a:
        if a[i]>M[0]:
            M=[a[i],i]
    for i in a:
        if a[i]<m[0] and i!=M[1]:
            m=[a[i],i]
    a[M[1]]-=a[m[1]]
    if a[M[1]]==0:a.pop(M[1])
    a.pop(m[1])
if a:
    print(max(a.values())-1)
else:
    print(0)