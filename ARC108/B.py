#!/usr/bin/python3

n=int(input())
s=list(input())
ans=[]
for i in s:
    ans.append(i)
    if len(ans)>2 and ans[-3:]==["f","o","x"]:
            for j in range(3):
                ans.pop(-1)
print(len(ans))