#!/usr/bin/python3

N=int(input())
S=[[*map(int,input())] for i in range(N)]
num={i:set() for i in range(10)}
for i in S:
    for j in range(10):
        now=i[j]
        flag=1
        while flag:
            if j+10*(flag-1) in num[i[j]]:
                flag+=1
            else:
                num[i[j]].add(j+10*(flag-1))
                flag=0
ans=float("inf")
for i in range(10):
    ans=min(ans,max(num[i]))
print(ans)