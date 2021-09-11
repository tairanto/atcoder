#!/usr/bin/python3
n=int(input())
a=list(map(int,input().split()))
ans=[2*sum([a[i] for i in range(n) if i%2==0])-sum(a)]
for i in range(n-1):
    ans.append(2*(a[i]-ans[-1]//2))
print(*ans)