#!/usr/bin/python3

n=int(input())
x=[int(input()) for i in range(n)]
ans=[]
for i in x:
    flag=0
    for j in range(len(ans)):
        if ans[j]>=i:
            flag=1
            break
    if flag:
        ans.pop(j)
        ans.insert(j,i)
    else:
        ans.append(i)
print(len(ans))