#!/usr/bin/python3


a,b=map(list,input().split())
ans=-1000
import copy
L=[str(i) for i in range(10)]
for i in range(3):
    temp=copy.deepcopy(a)
    for j in L:
        if i==0 and j=="0":continue
        temp[i]=j
        ans=max(ans,int("".join(temp))-int("".join(b)))
for i in range(3):
    temp=copy.deepcopy(b)
    for j in L:
        if i==0 and j=="0":continue
        temp[i]=j
        ans=max(ans,int("".join(a))-int("".join(temp)))
print(ans)