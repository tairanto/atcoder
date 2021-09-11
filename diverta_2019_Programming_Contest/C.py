#!/usr/bin/python3

N=int(input())
ans=0
S={"A":0,"B":0,"AB":0}
for i in range(N):
    s=input()
    ans+=s.count("AB")
    if s[0]=="B" and s[-1]=="A":
        S["AB"]+=1
    elif s[0]=="B":
        S[s[0]]+=1
    elif s[-1]=="A":
        S[s[-1]]+=1
print(ans+min(S["A"],S["B"])+S["AB"]-(S["A"]+S["B"]==0)*(S["AB"]>0))