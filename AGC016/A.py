#!/usr/bin/python3

s=list(input())
S={chr(i):[] for i in range(97,97+26)}
for i in S:
    count=0
    for j in s:
        if i==j:
            S[i].append(count)
            count=0
        else:
            count+=1
    S[i].append(count)
    S[i]=max(S[i])
print(min(S.values()))