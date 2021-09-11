#!/usr/bin/python3


N,M=map(int,input().split())
X=list(map(int,input().split()))
X.sort()
Y=[X[i+1]-X[i] for i in range(M-1)]
Y.sort()
if M-N<0:
    print(0)
else:
    print(sum(Y[:M-N]))