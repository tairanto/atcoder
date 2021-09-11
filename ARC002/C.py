#!/usr/bin/python3

N=int(input())
c=list(input())
S=[i+j for i in ["A","B","X","Y"]for j in ["A","B","X","Y"]]
ans=float("inf")
for i in range(len(S)):
    for j in range(len(S)):
        if i==j:continue
        cnt=N
        flag=0
        for k in range(N-1):
            if flag:
                flag=0
                continue
            if c[k]+c[k+1]==S[i] or c[k]+c[k+1]==S[j]:
                flag=1
                cnt-=1
        ans=min(ans,cnt)
print(ans)