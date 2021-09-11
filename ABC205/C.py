#!/usr/bin/python3

A,B,C=map(int,input().split())
if C%2:
    if A<0 and B>=0:
        print("<")
    elif A>=0 and B<0:
        print(">")
    else:
        if A==B:print("=")
        elif A>B:print(">")
        else:print("<")
else:
    A,B=abs(A),abs(B)
    if A==B:print("=")
    elif A>B:print(">")
    else:print("<")