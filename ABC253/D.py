#!/usr/bin/python3

def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)

N,A,B=map(int,input().split())
temp=GCD(A,B)
C=(A//temp)*(B//temp)*temp
a=A*(N//A)*(N//A+1)//2
b=B*(N//B)*(N//B+1)//2
c=C*(N//C)*(N//C+1)//2
print(N*(N+1)//2-a-b+c)