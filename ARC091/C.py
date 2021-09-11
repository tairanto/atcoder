#!/usr/bin/python3


h,w=map(int,input().split())
print([h-2 if h>1 else 1][0]*[w-2 if w>1 else 1][0])