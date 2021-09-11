#!/usr/bin/python3

n=int(input())
x=[list(map(int,input().split())) for i in range(n)]
cnt=0
for i in range(n):
    x1,y1=x[i][1]+(x[i][0]==3 or x[i][0]==4)/10,x[i][2]-(x[i][0]==2 or x[i][0]==4)/10
    for j in range(i+1,n):
        if i==j:continue
        x2,y2=x[j][1]+(x[j][0]==3 or x[j][0]==4)/10,x[j][2]-(x[j][0]==2 or x[j][0]==4)/10
        if x1<=x2:
            if x2<=y1 or y2<=y1:
                cnt+=1
        else:
            if x1<=y2 or y1<=y2:
                cnt+=1
print(cnt)