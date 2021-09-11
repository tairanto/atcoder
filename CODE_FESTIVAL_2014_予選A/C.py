#!/usr/bin/python3

a,b=map(int,input().split())
print(b//4-a//4+(a%4==0)-(b//100-a//100+(a%100==0))+b//400-a//400+(a%400==0))