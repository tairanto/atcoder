#!/usr/bin/python3
N=int(input())
x=list(map(int,input().split()))+[10**5+3,10**5+6]
X={}
for i in x:
    if i in X:
        X[i]+=1
    else:
        X[i]=1
s=sorted(X)
count=0
for i in range(len(s)-2):
    if s[i]+1==s[i+1]:
        if s[i+1]==s[i+2]-1 and count<X[s[i]]+X[s[i+1]]+X[s[i+2]]:
            count=X[s[i]]+X[s[i+1]]+X[s[i+2]]
        elif s[i+1]!=s[i+2]-1 and count<X[s[i]]+X[s[i+1]]:
            count=X[s[i]]+X[s[i+1]]
    elif s[i]+2==s[i+1] and count<X[s[i]]+X[s[i+1]]:
        count=X[s[i]]+X[s[i+1]]
    elif count<X[s[i]]:
        count=X[s[i]]
print(count)