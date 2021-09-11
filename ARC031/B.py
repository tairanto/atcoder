#!/usr/bin/python3

island=[list(input())+[0] for _ in range(10)]+[[0 for _ in range(11)]]
n=1
for i in range(10):
    for j in range(10):
        if island[i][j]=="x":
            island[i][j]=0
            continue
        if island[i][j]=="o":
            island[i][j]=n
            same=[[i,j]]
            while same:
                x,y=same.pop(-1)
                if island[x-1][y]=="o":
                    same.append([x-1,y])
                    island[x-1][y]=n
                if island[x][y-1]=="o":
                    same.append([x,y-1])
                    island[x][y-1]=n
                if island[x+1][y]=="o":
                    same.append([x+1,y])
                    island[x+1][y]=n
                if island[x][y+1]=="o":
                    same.append([x,y+1])
                    island[x][y+1]=n
            n+=1

for i in range(10):
    for j in range(10):
        if island[i][j]==0:
            if len(set([island[i-1][j],island[i][j-1],island[i+1][j],island[i][j+1],island[i][j]]))==n:
                print("YES")
                exit()
print("NO")