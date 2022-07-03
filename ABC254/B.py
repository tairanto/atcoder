#!/usr/bin/python3

ans=[[0,1,0]]
for i in range(30):
    temp=[0]
    for j in range(len(ans[-1])-1):
        temp.append(ans[-1][j]+ans[-1][j+1])
    temp.append(0)
    ans.append(temp)
for i in range(int(input())):
    print(*ans[i][1:-1])