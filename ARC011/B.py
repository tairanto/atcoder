#!/usr/bin/python3

num={"b":1,"c":1,"d":2,"w":2,"t":3,"j":3,"f":4,"q":4,"l":5,"v":5,"s":6,"x":6,"p":7,"m":7,"h":8,"k":8,"n":9,"g":9,"z":0,"r":0}

N=int(input())
w=input().split()
ans=[]
for i in w:
    temp=[num[j.lower()] for j in i if j.lower() in num]
    if len(temp)==0:continue
    ans.append(temp)
for i in range(len(ans)):
    if 0<i<len(ans):print(" ",end="")
    print(*ans[i],sep="",end="")
print()
    