#!/usr/bin/python3

A,B,C=map(int,input().split())
print(min((C-(C//2)*2)*A*B,(A-(A//2)*2)*B*C,(B-(B//2)*2)*A*C))
