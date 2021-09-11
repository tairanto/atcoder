#!/usr/bin/python3

s=list(input())
if "S" in s and not "N" in s:
    print("No")
    exit()
if "N" in s and not "S" in s:
    print("No")
    exit()
if "E" in s and not "W" in s:
    print("No")
    exit()
if "W" in s and not "E" in s:
    print("No")
    exit()
print("Yes")