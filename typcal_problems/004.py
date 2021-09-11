#!/usr/bin/python3

H,W=map(int,input().split())
A=[list(map(int,input().split())) for i in range(H)]
tate=[sum([A[j][i] for j in range(H)]) for i in range(W)]
yoko=[sum(A[i]) for i in range(H)]
for i in range(H):
    print(*[yoko[i]+tate[j]-A[i][j] for j in range(W)])