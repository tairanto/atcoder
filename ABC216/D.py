#!/usr/bin/python3

N,M=map(int,input().split())
ball={i+1:[2,0,0] for i in range(N)}#1:数2:1つ目の場所
k=[]
for i in range(M):
    ki=int(input())
    a=[i,[*map(int,input().split())]]
    k.append(a)
num=N*2
remove=[]
for i in range(M):
    b=k[i][1].pop(-1)
    ball[b][0]-=1
    if ball[b][0]:
        ball[b][1]=k[i][0]
    else:
        ball[b][2]=k[i][0]
        remove.append(b)
while remove:
    R=remove.pop(-1)
    f,s=ball[R][1],ball[R][2]
    ball.pop(R)
    if k[f][1]:
        b=k[f][1].pop(-1)
        ball[b][0]-=1
        if ball[b][0]:
            ball[b][1]=k[f][0]
        else:
            ball[b][2]=k[f][0]
            remove.append(b)
    if k[s][1]:
        b=k[s][1].pop(-1)
        ball[b][0]-=1
        if ball[b][0]:
            ball[b][1]=k[s][0]
        else:
            ball[b][2]=k[s][0]
            remove.append(b)
if ball:
    print("No")
else:
    print("Yes")