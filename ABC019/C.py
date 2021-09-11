#!/usr/bin/python3


N=int(input())
A=sorted([*map(int,input().split())])
a=set(A)
ans,now=0,0
while a:
    if A[now] in a:
        ans+=1
        n=A[now]
        while n<=10**9:
            if n in a:
                a.remove(n)
            n*=2
    now+=1
print(ans)