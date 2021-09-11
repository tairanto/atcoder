#!/usr/bin/python3

n=int(input())
num={}
for i in list(map(int,input().split())):
    temp=i//400
    if temp>7:temp=8
    if not temp in num:
        num[temp]=0
    num[temp]+=1
if 8 in num:
    print(len(num)-1+(len(num)==1),len(num)-1+num[8])
else:
    print(len(num),len(num))