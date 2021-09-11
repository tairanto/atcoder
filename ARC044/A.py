#!/usr/bin/python3

def prime(x):
    for i in range(2,int((x)**0.5)+1):
        if x%i==0:
            return False
    return True

n=input()
if n=="1":
    print("Not Prime")
    exit()
if prime(int(n)):
    print("Prime")
else:
    n=list(n)
    if int(n[-1])%2==0 or n[-1]=="5" or sum([int(i) for i in n])%3==0:
        print("Not Prime")
    else:
        print("Prime")