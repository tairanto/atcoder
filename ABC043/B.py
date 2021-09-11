#!/usr/bin/python3


s=list(input())
ans=[]
for i in s:
    if len(ans)==0 and i=="B":continue
    if i=="0" or i=="1":ans.append(i)
    else:ans.pop(-1)
print(*ans,sep="")