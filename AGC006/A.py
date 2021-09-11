#!/usr/bin/python3



n=int(input())
s=list(input())
t=list(input())
if s==t:
    print(n)
    exit()
for i in range(n):
    temp=s[:i]+t
    if temp[:n]==s and temp[-n:]==t:
        print(len(temp))
        exit()
print(2*n)