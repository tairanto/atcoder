#!/usr/bin/python3

X,A,D,N=map(int,input().split())
r=[A,A+D*(N-1)]
if D and min(r)<= X <= max(r):
    print(min((X-A)%abs(D),abs(D)-(X-A)%abs(D)))
else:
    print(min(abs(r[0]-X),abs(r[1]-X)))
