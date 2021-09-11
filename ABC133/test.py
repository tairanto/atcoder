#!/usr/bin/python3
def serch_2():
    return 0

n=int(input())
x=list(map(int,input().split()))
top=10**9
botom=0
while top-botom>1:
    mid=(top-botom)//2
    if ok(mid):break
    else:
