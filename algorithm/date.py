#!/usr/bin/python3

import datetime
N=int(input())
day=[]
for i in range(1,13):
    if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
        day.append([0 for _ in range(31)])
    elif i==2:
        day.append([0 for _ in range(29)])
    else:
        day.append([0 for _ in range(30)])
md=[list(map(int,input().split("/"))) for i in range(N)]
for i in md:
    day[i[0]-1][i[1]-1]=1
cnt=0
for i in range(1,13):
    for j in range(1,len(day[i-1])+1):
        if datetime.date(2012, i, j).weekday()==5 or datetime.date(2012, i, j).weekday()==6:
            if day[i-1][j-1]==1:
                cnt+=1
            else:
                day[i-1][j-1]=1
        else:
            if cnt and day[i-1][j-1]==0:
                day[i-1][j-1]=1
                cnt-=1
cnt=0
ans=0
for i in range(1,13):
    for j in range(1,len(day[i-1])+1):
        if cnt:
            if day[i-1][j-1]:
                cnt+=1
            else:
                ans=max(ans,cnt)
                cnt=0
        if cnt==0 and day[i-1][j-1]:
            cnt=1
print(max(ans,cnt))