#!/usr/bin/python3


N,M=map(int,input().split())
ans={i+1:0 for i in range(N)}
for i in range(M):
    a,b=map(int,input().split())
    if a<b:
        ans[b]+=1
    else:
        ans[a]+=1
print(sum([1 for i in ans if ans[i]==1]))