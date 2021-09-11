#!/usr/bin/python3


n,l=map(int,input().split())
grid={i:set() for i in range(l)}
for i in range(l+1):
    count=0
    for j in list(input()):
        if i==l:
            if j==" ":count+=1
            elif j=="o":ans=count//2
            continue
        if j=="|":count+=1
        elif j=="-":
            grid[i].add(count)
for i in range(l):
    if ans in grid[l-1-i]:
        ans-=1
    elif ans+1 in grid[l-1-i]:
        ans+=1
print(ans+1)