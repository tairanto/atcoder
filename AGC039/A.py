#!/usr/bin/python3


s=list(input())
k=int(input())
if s.count(s[0])==len(s):
    print(len(s)*k//2)
    exit()
s=s*min(k,3)
cnt=0
for i in range(1,len(s)-1):
    if s[i]==s[i+1]==s[i-1]:
        s[i]="#"
        cnt+=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        s[i+1]="$"
        cnt+=1
if k<3:
    print(cnt)
else:
    mid,ex=0,0
    for i in range(len(s)):
        if s[i]!="$" and s[i]!="#":continue
        if len(s)//3<=i<2*len(s)//3:
            mid+=1
    print(mid*(k-3)+cnt)