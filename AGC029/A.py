#!/usr/bin/python3

s=list(input())
b,ans=0,0
for i in range(len(s)):
    if s[i]=="B":b+=1
    else:ans+=b
print(ans)