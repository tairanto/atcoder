#!/usr/bin/python3
n,d=map(int,input().split())
print(n//(d*2+1)+[0 if n%(d*2+1)==0 else 1][0])