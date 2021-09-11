#!/usr/bin/python3

N,K=map(int,input().split())
c=list(map(int,input().split()))
can={}
ans=0
for i in range(N):
    if not c[i] in can.keys():
        can[c[i]]=0
    can[c[i]]+=1
    if i==K-1:ans=max(len(can),ans)
    if i<K:continue
    can[c[i-K]]-=1
    if can[c[i-K]]==0:can.pop(c[i-K])
    ans=max(len(can),ans)
    if ans==K:break
print(ans)