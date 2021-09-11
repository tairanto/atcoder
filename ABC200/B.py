#!/usr/bin/python3
n,k=input().split()
for i in range(int(k)):
    if int(n)%200:
        n+="200"
    else:
        n=str(int(n)//200)
print(n)