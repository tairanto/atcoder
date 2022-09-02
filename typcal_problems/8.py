#!/usr/bin/python3
N=int(input())
s=list(input())
atcoder={"a":0,"t":1,"c":2,"o":3,"d":4,"e":5,"r":6}
ans=[0,0,0,0,0,0,0,1]
for i in range(N-1,-1,-1):
  if not s[i] in atcoder:continue
  num=atcoder[s[i]]
  ans[num]=(ans[num]+ans[num+1])%(10**9+7)
print(ans[0])