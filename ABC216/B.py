#!/usr/bin/python3

N=int(input())
name=[list(input().split()) for i in range(N)]
for i in range(N):
    for j in range(i+1,N):
        if name[i][0]==name[j][0] and name[i][1]==name[j][1]:
            print("Yes")
            exit()
print("No")