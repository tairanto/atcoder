#!/usr/bin/python3

N,K=map(int,input().split())
ans=[]
for x,i in enumerate(list(map(int,input().split()))):
    ans.append([i,x])
ans.sort()
M=K%N
Ans=[]
for i in ans:
    Ans.append([i[1],K//N+(M>0)])
    M-=1
Ans.sort()
for i in Ans:
    print(i[1])