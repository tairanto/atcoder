#!/usr/bin/python3

N,K=map(int,input().split())
A,B=[*map(int,input().split())],[*map(int,input().split())]
diff=sum([abs(A[i]-B[i]) for i in range(N)])

if K-diff<0 or (K-diff)%2:
    print("No")
else:
    print("Yes")
