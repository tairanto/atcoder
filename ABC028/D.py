#!/usr/bin/python3


N,K=map(int,input().split())
print((1+3*(N-1)+6*(K-1)*(N-K))/(N**3))