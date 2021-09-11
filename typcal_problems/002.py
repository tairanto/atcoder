#!/usr/bin/python3

n=int(input())
if n%2:exit()
for i in range(1<<n):
    temp=["(" if (i>>(n-1-j))%2==0 else ")" for j in range(n)]
    cnt=0    
    flag=1
    for j in temp:
        if j=="(":cnt+=1
        else:cnt-=1
        if cnt<0:
            flag=0
            break
    if flag and cnt==0:print(*temp,sep="")