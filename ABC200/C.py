#!/usr/bin/python3
n=int(input())
x=input().split()
num={}
for i in x:
    i=i.zfill(4)
    if not i[-2:] in num.keys():
        num[i[-2:]]=[[],[]]
    if int(i[:-2])%2==0:
        num[i[-2:]][0].append(int(i))
    else:
        num[i[-2:]][1].append(int(i))
ans=0
for i in num:
    for j in num[i]:
        J=len(j)
        if J<2:continue
        ans+=J*(J-1)//2
print(ans)