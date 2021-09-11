#!/usr/bin/python3

n=int(input())
s={"M":0,"A":0,"R":0,"C":0,"H":0}
for i in range(n):
    temp=input()
    if temp[0] in s:
        s[temp[0]]+=1
import itertools
c = itertools.combinations(list(s.keys()), 3)
ans=0
for i in c:
    temp=1
    for j in i:
        temp*=s[j]
    ans+=temp
print(ans)