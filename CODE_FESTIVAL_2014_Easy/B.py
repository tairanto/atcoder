#!/usr/bin/python3

n=int(input())-1
if (n//20)%2:
    print(20-n%20)
else:
    print(n%20+1)