#!/usr/bin/python3

N,X,Y=map(int,input().split())
ans=[0 for i in range(N-1)]
for i in range(1,N+1):
  for j in range(i+1,N+1):
    a=j-i
    b=abs(X-i)+abs(Y-j)+1
    ans[[a,b][a>b]-1]+=1
print(*ans,sep="\n")