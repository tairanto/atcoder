#!/usr/bin/python3

N=int(input())
sosuu=set([i for i in range(2,1001)])
[[sosuu.remove(i*j) for j in range(2,1001//2) if i*j in sosuu]for i in range(2,1001)]
ans={i:0 for i in sosuu}
sosuu=list(sosuu)
for i in range(2,N+1):
    temp=i
    now=0
    while temp!=1:
        if temp%sosuu[now]:
            now+=1
        else:
            ans[sosuu[now]]+=1
            temp//=sosuu[now]
A=1
for i in ans:
    A*=(ans[i]+1)
print(A%(10**9+7))
