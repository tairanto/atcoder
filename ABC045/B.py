#!/usr/bin/python3

a,b,c=list(input()),list(input()),list(input())
s="a"
while (1):

    if s=="a":
        if not a:
            print("A")
            exit()
        s=a.pop(0)
    elif s=="b":
        if not b:
            print("B")
            exit()
        s=b.pop(0)
    else:
        if not c:
            print("C")
            exit()
        s=c.pop(0)