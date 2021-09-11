#!/usr/bin/python3

N=int(input())
for i in range(1,N+1):
    score=i*(i+1)//2
    if score>=N:
        break
ans=[]
count=0
while N:
    if N-i>=0:
        N-=i
        ans.append(i)
    i-=1
print(*reversed(ans),sep="\n")