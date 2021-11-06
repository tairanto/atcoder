#!/usr/bin/python3


N,M=map(int,input().split())
S=[*map(int,input().split())]
T=[*map(int,input().split())]
if set(S)&set(T)!=set(T):
    print(-1)
    exit()
c=[-float("inf") for _ in range(N)]
one=-float("inf")
zero=-float("inf")
for x in range(2*N):
    i=x%N
    if S[i]==0:
        zero=0
    else:
        zero-=1
        c[i]=max(c[i],zero)
    if S[i]==1:
        one=0
    else:
        one-=1
        c[i]=max(c[i],one)
one=float("inf")
zero=float("inf")
for x in range(2*N):
    i=x%N
    if S[-1-i]==0:
        zero=0
    else:
        zero+=1
        if abs(c[-1-i])>zero:
            c[-1-i]=zero
    if S[-1-i]==1:
        one=0
    else:
        one+=1
        if abs(c[-1-i])>one:
            c[-1-i]=one
ans=0
now=0
zo=S[0]
for i in T:
    if zo==i:
        ans+=1
    else:
        ans+=abs(c[now])+1
        now=(now+c[now])%N
        zo=i
print(ans)