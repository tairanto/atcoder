#!/usr/bin/python3

N=int(input())
A=list(map(int,input().split()))
ave=sum(A)//N
if not sum(A)==N*ave:
    print(-1)
    exit()
now,count,ans=0,0,0
for i in A:
    now+=i
    count+=1
    if now==ave*count:
        now=0
        ans+=count-1
        count=0
print(ans)