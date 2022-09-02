#!/usr/bin/python3
def ok(mid,K):
  youkan=[A[0]]
  for i in A[1:]:
    if youkan[-1]<mid or len(youkan)>=K+1:
      youkan[-1]+=i
    else:
      youkan.append(i)
  if len(youkan)<K+1 or youkan[-1]<mid:
    return True
  else:
    return False

N,L=map(int,input().split())
K=int(input())
a=[*map(int,input().split())]+[L]
A=[a[0]]
for i in range(N):
  A.append(a[i+1]-a[i])
  
bottom=-1
top=L+1
while top-bottom>1:
  mid=(top+bottom)//2
  if ok(mid,K):
    top=mid
  else:
    bottom=mid
print(bottom)