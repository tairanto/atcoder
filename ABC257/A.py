#!/usr/bin/python3

s=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
n,k=map(int,input().split())
print(s[k//n-1+(k%n>0)])