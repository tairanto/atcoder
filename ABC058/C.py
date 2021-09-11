#!/usr/bin/python3

n=int(input())
ans={chr(i):50 for i in range(97, 97+26)}#ord("a")でintになる
for i in range(n):
    temp={chr(i):0 for i in range(97, 97+26)}
    for j in list(input()):
        temp[j]+=1
    for i in temp:
        ans[i]=min(ans[i],temp[i])
for i in range(97,97+26):
    print(ans[chr(i)]*chr(i),end="")
print()