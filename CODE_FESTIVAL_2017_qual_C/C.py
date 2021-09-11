#!/usr/bin/python3

s=input()
N=len(s)
f,b=0,-1
ans=0
while f<=N+b:
    if f==N+b:break
    if s[f]==s[b]:
        f+=1
        b-=1
    else:
        if s[f]=="x":
            f+=1
        elif s[b]=="x":
            b-=1
        else:
            print(-1)
            exit()
        ans+=1
print(ans)