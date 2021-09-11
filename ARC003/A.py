#!/usr/bin/python3

n=int(input())
s=list(input())
if s.count("F")==n:
    print(0)
    exit()
print((s.count("A")*4+s.count("B")*3+s.count("C")*2+s.count("D"))/n)