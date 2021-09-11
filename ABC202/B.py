#!/usr/bin/python3

s=list(input())
for i in reversed(s):
    if i=="0" or i=="1" or i=="8":
        print(i,end="")
    elif i=="9":
        print("6",end="")
    else:
        print("9",end="")
print()