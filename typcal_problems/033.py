#!/usr/bin/python3

H,W=map(int,input().split())
if H==1 or W==1:#は？
    print(H*W)
else:
    print((H//2+H%2)*(W//2+W%2))
