#!/usr/bin/python3

mtx=[list(map(int,input().split())) for i in range(3)]
for i in range(101):
    a1=i
    b1=mtx[0][0]-a1
    b2=mtx[0][1]-a1
    b3=mtx[0][2]-a1
    a2=mtx[1][0]-b1
    a3=mtx[2][0]-b1
    if b1<0 or b2<0 or b3<0 or a1<0 or a2<0:continue
    if mtx[1][1]!=a2+b2 or mtx[2][1]!=a3+b2 or mtx[1][2]!=a2+b3 or mtx[2][2]!=a3+b3:continue
    print("Yes")
    exit()
print("No")