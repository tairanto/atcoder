#!/usr/bin/python3
n=int(input())
x=list(map(int,input().split()))
ans=[0 for i in range(2*(10**5))]
cnt=0
for i in range(n):
    num=n-i-1
    #print(n//(num+1),[ans[(j+1)*(num+1)-1] for j in range(n//(num+1))])
    if x[n-1-i]%2:
        if sum([ans[(j+1)*(num+1)-1] for j in range(n//(num+1))])%2:continue
        else: ans[num]=1             
    else:
        if sum([ans[(j+1)*(num+1)-1] for j in range(n//(num+1))])%2==0:continue
        else: ans[num]=1
    if ans[num]:cnt+=1
if cnt:
    print(cnt)
    print(*[i+1 for i in range(n) if ans[i]])
else:
    print(0)