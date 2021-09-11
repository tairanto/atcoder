#!/usr/bin/python3

S=input()
ans=[]
for i in S:
    ans.append(i)
    if ans[-2:]==["S","T"]:
        ans.pop(-1)
        ans.pop(-1)
print(len(ans))