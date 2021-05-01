#!/usr/bin/python3
m,n,N=map(int,input().split())
amari,count=0,N
while N>=m:
    amari=N%m
    N=(N//m)*n
    count+=N
    N+=amari
print(count)