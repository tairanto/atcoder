#!/usr/bin/python3
N=int(input())
while N%2==0:
    N//=2
count=0
for i in range(1,int(N**0.5)+1):
    if N%i==0:
       count+=2
if i**2==N:
    count-=1
print(count*2)