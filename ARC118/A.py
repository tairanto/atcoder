#!/usr/bin/python3
t,n=map(int,input().split())
print((100+t)*n//t-((100+t)*n%t==0))
