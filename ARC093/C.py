#!/usr/bin/python3
n=int(input())
x=[0]+list(map(int,input().split()))+[0]
total=sum([abs(x[i+1]-x[i]) for i in range(n+1)])
for i in range(n):
    print(total-(abs(x[i]-x[i+1])+abs(x[i+1]-x[i+2])-abs(x[i]-x[i+2])))