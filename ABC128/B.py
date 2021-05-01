#!/usr/bin/python3
n=int(input())
x=[list(input().split()) for i in range(n)]
y={}
s=[]
for i in x:
    if i[0] in y:
        y[i[0]].append(int(i[1]))
    else:
        s.append(i[0])
        y[i[0]]=[int(i[1])]
s.sort()
for i in s:
    for j in sorted(y[i],reverse=True):
        for num,k in enumerate(x):
            if k[0]==i and k[1]==str(j):
                print(num+1)
                break