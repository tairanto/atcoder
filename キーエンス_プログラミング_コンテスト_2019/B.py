#!/usr/bin/python3

s=list(input())
n=len(s)
ans=["keyofscience","keyence"]
if n>12:
    for i in range(13):
        temp=s[:i]+s[i+n-12:]
        if "".join(temp)==ans[0]:
            print("YES")
            exit()
for i in range(8):
    temp=s[:i]+s[i+n-7:]
    if "".join(temp)==ans[1]:
        print("YES")
        exit()
print("NO")