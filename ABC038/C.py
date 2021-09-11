#!/usr/bin/python3

N=int(input())
A=[0]+list(map(int,input().split()))+[0]
con=0
ans=0
for i in range(1,N+2):
  if A[i-1]<A[i]:
    con+=1
  else:
    ans+=con*(con+1)//2
    con=1
print(ans)
