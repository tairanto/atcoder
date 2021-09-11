#!/usr/bin/python3

for i in range(int(input())):
    print(*reversed(input().translate(str.maketrans({'A': 'T', 'T': 'A','C': 'G', 'G': 'C'}))),sep="")