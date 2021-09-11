#!/usr/bin/python3

N=int(input())
student=[list(map(int,input().split())) for i in range(N)]
first,second=[0],[0]
for i in student:
    first.append(first[-1]+[0,i[1]][i[0]==1])
    second.append(second[-1]+[0,i[1]][i[0]==2])
Q=int(input())
for i in range(Q):
    L,R=map(int,input().split())
    print(first[R]-first[L-1],second[R]-second[L-1])