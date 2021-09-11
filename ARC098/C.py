#!/usr/bin/python3

#E->
#W<-
n=int(input())
s=list(input())
r,l=[0],[0]
for i in s:
    if i=="E":
        r.append(r[-1]+1)
    else:
        r.append(r[-1])
for i in range(n):
    if s[n-1-i]=="W":
        l.append(l[-1]+1)
    else:
        l.append(l[-1])
ans=float("inf")
for i in range(n+1):
    ans=min(ans,n-(r[i]+l[n-i]))
print(ans)