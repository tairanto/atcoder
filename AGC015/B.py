#!/usr/bin/python3

S=list(input())
N=len(S)
ans=0
for i in range(1,N+1):
    if S[i-1]=="U":
        ans+=N-i #上方向
        ans+=(i-1)*2 #下方向
    else:
        ans+=(N-i)*2 #上方向
        ans+=i-1 #下方向
print(ans)