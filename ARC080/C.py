#!/usr/bin/python3
n=int(input())
num={2:0,4:0,1:0}
for i in list(map(int,input().split())):
    if i%4==0:
        num[4]+=1
    elif i%2==0:
        num[2]+=1
    else:
        num[1]+=1
if num[1]>num[4]+1 or (num[1]==num[4]+1 and num[2]>0) or (num[4]==0 and num[2]==1):
    print("No")
else:
    print("Yes")