#!/usr/bin/python3
from math import gcd
A,B,C=map(int,input().split())
GCD=gcd(gcd(A,B),C)
print(A//GCD+B//GCD+C//GCD-3)