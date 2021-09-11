#!/usr/bin/python3

n=int(input())
combo=[0 for i in range(9)]
cnt=0
for i in range(n):
    temp=list(input())
    for i in range(9):
        if temp[i]=="x":
            if combo[i]:
              combo[i]=0
              cnt+=1
            cnt+=1
        elif temp[i]=="o":
            if combo[i]==0:
               combo[i]=1
        else:
            if combo[i]:
              combo[i]=0
              cnt+=1
print(cnt+sum([1 for i in combo if i]))