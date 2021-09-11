#!/usr/bin/python3

s=list(input())
k=int(input())
for x,i in enumerate(s):
    if i=="1":
        if k==x+1:
            ans=1
            break
    else:
        ans=i
        break
print(ans)