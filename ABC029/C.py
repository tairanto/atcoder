#!/usr/bin/python3

def add(x):
    temp=[]
    for i in x:
        for j in l:
            temp.append(i+j) 
    return temp
    
n=int(input())
l=["a","b","c"]
ans=["a","b","c"]
for i in range(n-1):
    ans=add(ans)
print(*ans,sep="\n")