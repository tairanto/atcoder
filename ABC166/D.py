#!/usr/bin/python3

x=int(input())
for i in range(-120,121):
    for j in range(-120,121):
        if i**5==x+j**5:
            print(i,j)
            exit()