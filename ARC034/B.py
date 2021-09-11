#!/usr/bin/python3

N=int(input())
ans=[i for i in range(max(0,N-200),N) if i+sum([int(i) for i in str(i)])==N]
print(len(ans))
if ans:
    print(*ans,sep="\n")