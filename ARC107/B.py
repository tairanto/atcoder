#!/usr/bin/python3

N,K=map(int,input().split())
x=[0,0]
for i in range(2,2*N+1):
    if i>N+1:
        x.append(x[-1]-1)
    else:
        x.append(x[-1]+1)
ans=0
for i in range(2,2*N+1):
    ab=i
    cd=i-K
    if cd>2*N:break
    if cd<2:continue
    ans+=x[ab]*x[cd]
print(ans)