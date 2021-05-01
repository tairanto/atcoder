#!/usr/bin/python3
n,x,y=map(int,input().split())
A,B=input().split(),input().split()
ans=10**9
import copy
temp=copy.deepcopy(B)
a=A.count("R")
ori=["R" if a<n-a else "B"]
for i in range(1<<n):
    money,flag=0,0
    if not i==0:B=copy.deepcopy(temp)
    #RB数合わせ 操作y　bit全探索
    for j in range(n):
        if (i>>(n-1-j))%2==1:
            money+=y
            if B[j]==A[j]:
                flag=1
                break
            else:
                B[j]=A[j]
    b=B.count("R")
    if flag or not a==b:continue
    #操作x　
    a_in,b_in=[],[]
    for j in range(n):
        if A[j]==ori[0] and B[j]==ori[0]:continue
        if A[j]==ori[0]:a_in.append(j)    
        if B[j]==ori[0]:b_in.append(j)
    ans=min(ans,money+x*sum([abs(a_in[j]-b_in[j]) for j in range(len(a_in))]))
print(ans)