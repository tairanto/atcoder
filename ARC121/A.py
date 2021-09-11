#!/usr/bin/python3

N=int(input())
x,y=[],[]
for i in range(N):
    a,b=map(int,input().split())
    x.append([a,b,i])
    y.append([b,a,i])
x.sort()
y.sort()
ans=[[x[-1][0]-x[0][0],(x[-1][2],x[0][2])],[x[-2][0]-x[0][0],(x[-2][2],x[0][2])],[x[-1][0]-x[1][0],(x[-1][2],x[1][2])],
     [y[-1][0]-y[0][0],(y[-1][2],y[0][2])],[y[-2][0]-y[0][0],(y[-2][2],y[0][2])],[y[-1][0]-y[1][0],(y[-1][2],y[1][2])]]
ans.sort(reverse=True)
first=ans[0]
for i in ans[1:]:
    if first[1]==i[1]:continue
    print(i[0])
    exit()