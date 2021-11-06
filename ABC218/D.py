#!/usr/bin/python3

N=int(input())
X={}
Y={}
for i in range(N):
    x,y=map(int,input().split())
    if not x in X:
        X[x]=[]
    if not y in Y:
        Y[y]=set()
    X[x].append(y)
    Y[y].add(x)
ans=0
for i in X:
    if len(X[i])<2:continue
    for k in range(len(X[i])):
        for l in range(k+1,len(X[i])):
            y1,y2=X[i][k],X[i][l]
            ans+=len(Y[y1]&Y[y2])-1
print(ans//2)