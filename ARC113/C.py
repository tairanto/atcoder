#!/usr/bin/python3
s=list(input())
x=[]
ans=0
S={}
for i in range(len(s)):
    x.append(s[-1-i])
    if not s[-1-i] in S.keys():
        S[s[-1-i]]=0
    S[s[-1-i]]+=1
    if i>1 and x[-1]==x[-2]:
        ans+=len(x)-S[x[-1]]
        S={x[-1]:len(x)}
print(ans)