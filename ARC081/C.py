#!/usr/bin/python3

n=int(input())
x=list(map(int,input().split()))+[0,0,0,0]
x.sort(reverse=True)
squre=[]
for i in range(n+3):
    if x[i]==x[i+1]:
        squre.append(x[i])
        x[i+1]=-1
    if len(squre)==2:
        break
print(squre[0]*squre[1])