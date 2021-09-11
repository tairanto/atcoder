#!/usr/bin/python3

H,W=map(int,input().split())
s=[list(input())+["#"] for _ in range(H)]+[["#"]*(W+1)]
ans=sum([sum([1 for j in range(W) if s[i][j]=="."]) for i in range(H)])
import queue
que=queue.Queue()
que.put([0,0])
s[0][0]=1
while not que.empty():
    x,y=que.get()
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i*j==1 or i*j==-1 or (i==0 and j==0):continue
            if s[x+i][y+j]!="#" and (s[x+i][y+j]=="." or s[x+i][y+j]>s[x][y]+1):
                s[x+i][y+j]=s[x][y]+1
                que.put([x+i,y+j])
if s[H-1][W-1]==".":
    print(-1)
else:
    print(ans-s[H-1][W-1])