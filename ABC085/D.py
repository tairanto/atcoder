#!/usr/bin/python3


N,H=map(int,input().split())
A,B=[],[]
M=[0,0]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append([b,i])
    if a>M[1]:
        M=[i,a,b]
    elif a==M[1] and b<M[2]:
        M=[i,a,b]
A.sort()
B.sort()
if A[-1]>=B[-1][0]:
    print(H//A[-1]+(H%A[-1]>0))
    exit()
ans=0
while H>0:
    if H<=M[2]:
        ans+=1
        break
    if B and B[-1][0]>=M[1]:
        if B[-1][1]!=M[0]:
            H-=B[-1][0]
            ans+=1
        B.pop(-1)
    else:
        if M[1]<M[2]:
            ans+=1
            H-=M[2]
        ans+=H//M[1]+(H%M[1]>0)
        break
print(ans)