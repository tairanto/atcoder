#!/usr/bin/python3

N=int(input())
L=[]
for i in range(N):
  s,l=map(int,input().split())
  L.append([s+l,s-l])
L.sort()
ans=1
end=L[0][0]
for i in range(1,N):
  if end<=L[i][1]:
    end=L[i][0]
    ans+=1
print(ans)