#!/usr/bin/python3

H,W=map(int,input().split())
after=[list(input())+["#"] for i in range(H)]+[["#" for i in range(W+1)]]
before=[["." for i in range(W)] for j in range(H)]
for i in range(H):
    for j in range(W):
        if after[i][j]==".":continue
        flag=1
        for k in range(-1,2):
            for l in range(-1,2):
                if after[i+k][j+l]==".":
                    flag=0
                    break
            if not flag:break
        if flag:before[i][j]="#"

for i in range(H):
    for j in range(W):
        if after[i][j]==".":continue
        flag=1
        for k in range(-1,2):
            if (i==0 and k==-1) or (i==H-1 and k==1) :continue
            for l in range(-1,2):
                if (j==0 and l==-1) or (j==W-1 and l==1) :continue
                if before[i+k][j+l]=="#":
                    flag=0
                    break
            if not flag:break
        if flag:
            print("impossible")
            exit()
print("possible")
for i in before:
    print(*i,sep="")