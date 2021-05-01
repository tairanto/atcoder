#!/usr/bin/python3
n,k=map(int,input().split())
a=list(map(int,input().split()))
e,cnt,score=0,0,0
for i in range(n):
    flag=1
    for j in range(e,n):
        if score+a[j]<k:
            score+=a[j]
        else:
            cnt+=n-j
            e=j
            flag=0
            score-=a[i]
            break
    if flag:break
print(cnt)