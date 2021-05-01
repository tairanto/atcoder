#!/usr/bin/python3
n,m=map(int,input().split())
k=[list(map(int,input().split())) for i in range(m)]
switch={i+1:[] for i in range(n)}
for i in range(m):
    for j in k[i][1:]:
        switch[j].append(i)
p=list(map(int,input().split()))
cnt=0
for i in range(1<<n):
    temp=[0 for i in range(m)]
    for j in range(n):
        if (i>>j)%2==1:
            for l in switch[n-j]:
                temp[l]+=1
    flag=1
    for j in range(m):
        if not temp[j]%2==p[j]:
            flag=0
            break
    if flag:cnt+=1
print(cnt)