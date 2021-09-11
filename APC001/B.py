#!/usr/bin/python3

N=int(input())
A,B=[*map(int,input().split())],[*map(int,input().split())]
diff=abs(sum(A)-sum(B))
a,b=0,0
for i in range(N):
    if A[i]<B[i]:
        if (B[i]-A[i])%2:
            a+=(B[i]-A[i])//2+1
            b+=1
        else:
            a+=(B[i]-A[i])//2
    else:
        b+=A[i]-B[i]
if a>b:
    x=a-b
    a+=x
    b+=x*2
if a==b==diff:
    print("Yes")
else:
    print("No")