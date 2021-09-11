#!/usr/bin/python3

s=list(input())
if len(s)==1:
    if s[0]=="8":print("Yes")
    else:print("No")
elif len(s)==2:
    if int(s[0]+s[1])%8==0 or int(s[1]+s[0])%8==0:print("Yes")
    else:print("No")
else:
    num={i+1:0 for i in range(9)}
    for i in s:
        num[int(i)]+=1
    eight=[i for i in range(100,1000) if i%8==0]
    for i in eight:
        E=[0 for i in range(10)]
        temp=list(str(i))
        if "0" in temp:continue
        for j in temp:
            E[int(j)]+=1
        flag=1
        for j in range(1,10):
            if E[j]>num[j]:
                flag=0
                break
        if flag:
            print("Yes")
            exit()
    print("No")