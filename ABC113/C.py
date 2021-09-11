#!/usr/bin/python3

N,M=map(int,input().split())
n=[0 for i in range(N+1)]
PY=[[i]+list(map(int,input().split())) for i in range(M)]
PY.sort(key=lambda x:x[2])
for i in range(M):
  n[PY[i][1]]+=1
  PY[i].append(str(PY[i][1]).zfill(6)+str(n[PY[i][1]]).zfill(6))
for i in sorted(PY):
  print(i[3])