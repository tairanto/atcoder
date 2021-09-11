#!/usr/bin/python3

n=int(input())
x,total=[],0
for i in range(n):
    temp=int(input())
    total+=temp
    if temp%10:
        x.append(temp)
if total%10:
    print(total)
else:
    if len(x)==0:
        print(0)
    else:
        x.sort()
        print(total-x[0])