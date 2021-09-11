#!/usr/bin/python3

from math import pi
x=sorted([*map(int,input().split())],reverse=True)
OA,AB,BC=x
print(((OA+AB+BC)**2-max(0,OA-AB-BC)**2)*pi)