#!/usr/bin/python3

a=[*map(int,input().split())]
ans=[chr(96+i) for i in a]
print(*ans,sep="")