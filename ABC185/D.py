#!/usr/bin/python3

n,m=map(int,input().split())
a=list(map(int,input().split()))+[0,n+1]
a.sort()
total=[]
for i in range(m+1):
    temp=a[i+1]-a[i]-1
    if temp<=0:continue
    total.append(temp)
if len(total)==0:
    print(0)
    exit()
Min=min(total)
print(sum([i//Min+(i%Min>0) for i in total]))