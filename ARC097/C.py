#!/usr/bin/python3

S=list(input())
N=int(input())
s=set()
for i in range(len(S)):
    temp=S[i]
    s.add(temp)
    for j in range(i+1,min(i+6,len(S))):
        temp+=S[j]
        s.add(temp)
print(sorted(list(s))[N-1])