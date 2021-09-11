#!/usr/bin/python3
    
def Y(N):
    for i in range(1,int(N**0.5)+1):
        if N%i==0:
            yakusuu.add(i)
            yakusuu.add(N//i)

N,M=map(int,input().split())
A=sorted([*map(int,input().split())])
yakusuu=set()
for i in A:
    if i==1:continue
    Y(i)
ans=[0 for i in range(M)]
for i in yakusuu:
    if i==1:continue
    for j in range(M//i):
        ans[(j+1)*i-1]=1
ans=[x+1 for x,i in enumerate(ans) if i==0]
print(len(ans),*ans,sep="\n")