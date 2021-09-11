#!/usr/bin/python3

n=int(input())
a=list(map(int,input().split()))
b=[2 if i%2 else 1 for i in a]
ans=0
for i in range((1<<n)-1):
    temp=1
    for j in range(n):
        if (i>>j)%2:
            temp*=3-b[j]
        else:
            temp*=b[j]
    ans+=temp
print(ans)
