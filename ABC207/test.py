#!/usr/bin/python3
from math import sin,cos,radians
n=int(input())
S,T=[list(map(int,input().split())) for i in range(n)],[list(map(int,input().split())) for i in range(n)]
t=[[0 for i in range(30)]for j in range(30)]
for i in T:
    t[10+i[0]][10+i[1]]=1
num=set([float(i) for i in range(-10,11)])
dist={}
for i in range(1,n):
    d=(T[i][0]-T[0][0])**2+(T[i][1]-T[0][1])**2
    if not d in dist:
        dist[d]=0
    dist[d]+=1
for i in range(n):
    temp={k:0 for k in dist.keys()}
    flag=1
    for j in range(n):
        if i==j:continue
        d=(S[i][0]-S[j][0])**2+(S[i][1]-S[j][1])**2
        if not d in temp:
            flag=0
            break
        temp[d]+=1
    if flag==0:continue
    if not temp==dist:continue
    if i!=1:continue
    for k in range(1,360):
        r=radians(k)
        flag=1
        for j in range(n):
            if i==j:continue
            x,y=S[j][0]-S[i][0],S[j][1]-S[i][1]
            cx,cy=x*cos(r)-y*sin(r)+T[0][0],x*sin(r)+y*cos(r)+T[0][1]
            if k==270:
                print(cx,cy)
            if not (cx in num and cy in num):
                flag=0
                break
            print(cx,cy,k,j)
            if t[int(cx)+10][int(cy)+10]==0:
                flag=0
                break
        if flag:
            print("Yes")
            exit()
print("No")