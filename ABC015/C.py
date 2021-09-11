#!/usr/bin/python3

N,K=map(int,input().split())
x=[[0 for i in range(5)] for j in range(5)]
for i in range(N):
    T=[*map(int,input().split())]
    for j in range(K):
        x[i][j]=T[j]
for i in range(min(5,K)):
    for j in range(min(5,K)):
        for k in range(min(5,K)):
            for l in range(min(5,K)):
                for m in range(min(5,K)):
                    ans=x[0][i]
                    if N>1:ans^=x[1][j]
                    if N>2:ans^=x[2][k]
                    if N>3:ans^=x[3][l]
                    if N>4:ans^=x[4][m]
                    if ans==0:
                        print("Found")
                        exit()
print("Nothing")