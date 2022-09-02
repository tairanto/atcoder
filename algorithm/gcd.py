#!/usr/bin/python3
def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)

def main():
    print(GCD(81,30))

main()