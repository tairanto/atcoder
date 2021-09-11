#!/usr/bin/python3

N=int(input())
ans=""
while N>0 and len(ans)<121:
    if N%2==0:
        N//=2
        ans+="B"
    else:
        N-=1
        ans+="A"
print(*reversed(ans),sep="")