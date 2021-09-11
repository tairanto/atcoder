#!/usr/bin/python3

x=list(map(int,input().split()))
ans=[0 for i in range(501)]
for i in range(5):
    for j in range(i+1,5):
        for k in range(j+1,5):
            ans[x[i]+x[j]+x[k]]=1
cnt=0
for i in range(501):
    if ans[500-i]:
        cnt+=1
        if cnt==3:
            break
print(500-i)