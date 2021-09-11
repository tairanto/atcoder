#!/usr/bin/python3

S,K=input().split()
import itertools
ans=set()
for i in itertools.permutations(S, len(S)):
    ans.add("".join(i))
ans=list(ans)
print(sorted(ans)[int(K)-1])