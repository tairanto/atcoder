#!/usr/bin/python3

n=int(input())
s=list(input())
if n%2:
    print(-1)
    exit()
print(n//2-sum([1 for i in range(n//2) if s[i]==s[i+n//2]]))