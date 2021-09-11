#!/usr/bin/python3

n=int(input())
for x,i in enumerate(list(input())):
    if i=="1":
        if x%2==0:
            print("Takahashi")
        else:
            print("Aoki")
        break