#!/usr/bin/python3
n=int(input())
x=list(map(int,input().split()))
x=[i%200 for i in x]
ans={}
e=0
for i in range(1<<min(8,n)):
    temp=sum([x[j] for j in range(min(8,n)) if (i>>j)%2])%200
    if not temp in ans:
        ans[temp]=[]
    ans[temp].append(i)
for i in reversed(ans):
    cnt=len(ans[i])
    if cnt==1:continue
    for j in range(cnt):
        for k in range(1,cnt):
            X=[l+1 for l in range(min(8,n)) if (ans[i][j]>>l)%2]
            Y=[l+1 for l in range(min(8,n)) if (ans[i][k]>>l)%2]
            if sum([1 for k in range(min(len(X),len(Y))) if X[k]==Y[k]]):continue
            if len(X)==0:continue
            print("Yes")
            print(len(X),*X)
            print(len(Y),*Y)
            exit()
print("No")