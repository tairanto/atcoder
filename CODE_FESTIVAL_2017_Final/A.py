#!/usr/bin/python3

s=list(input())
x=["A","K","I","H","A","B","A","R","A",""]
cnt=0
flag=1
for i in s:
    if x[cnt]=="A":
        if i=="A":
            cnt+=1
        else:
            if i==x[cnt+1]:
                cnt+=2
            else:
                flag=0
                break
    else:
        if i==x[cnt]:
            cnt+=1
        else:
            flag=0
            break
if flag and cnt>7:
    print("YES")
else:
    print("NO")