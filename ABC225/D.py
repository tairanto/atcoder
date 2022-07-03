#!/usr/bin/python3
n,m=map(int,input().split())
train=[[0,0] for i in range(n)]
for i in range(m):
    q=[*map(int,input().split())]
    if q[0]==1:
        train[q[1]-1][1]=q[2]
        train[q[2]-1][0]=q[1]
    elif q[0]==2:
        train[q[1]-1][1],train[q[2]-1][0]=0,0
    else:
        ans=[[],[]]
        top,back=q[1],q[1]
        while top or back:
            if top:
                ans[0].append(top)
                top=train[top-1][0]
            if back:
                ans[1].append(back)
                back=train[back-1][1]
        print(len(ans[0])+len(ans[1])-1,*[i for i in reversed(ans[0])],*ans[1][1:])

