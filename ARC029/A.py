#!/usr/bin/python3

n=int(input())
niku=[int(input()) for i in range(n)]
ans=300
for i in range(1<<n):
    t1,t2=0,0
    for j in range(n):
        if (i>>j)%2:
            t1+=niku[j]
        else:
            t2+=niku[j]
    ans=min(ans,max(t1,t2))
print(ans)