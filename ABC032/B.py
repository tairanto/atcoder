#!/usr/bin/python3

s=list(input())
K=int(input())
ans={}
for i in range(len(s)):
    temp="".join(s[i:i+K])
    if len(temp)==K and not temp in ans:
        ans[temp]=0
print(len(ans))