#!/usr/bin/python3
def check(x,y):
  for i in range(M):
    for j in range(M):
      if n[x+i][y+j]!=m[i][j]:
        return False
  return True

N,M=map(int,input().split())
n,m=[list(input()) for _ in range(N)],[list(input()) for _ in range(M)]
for i in range(N-M+1):
  for j in range(N-M+1):
    if check(i,j):
      print("Yes")
      exit()
print("No")
