#!/usr/bin/python3

n=int(input())
x=list(map(int,input().split()))
ans,flag,now=1,0,x[0]
for i in x[1:]:
    if flag==0 and now>i:
        flag=-1
    elif flag==0 and now<i:
        flag=1
    elif flag==-1 and now<i:
        ans+=1
        flag=0
    elif flag==1 and now>i:
        ans+=1
        flag=0
    now=i
print(ans)