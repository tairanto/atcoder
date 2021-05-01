#!/usr/bin/python3
a,b,k=map(int,input().split())
k*=1000
M,m=k//a,k//b
if a==b:
    if k%a:
        print("UNSATISFIABLE")
    else:
        print(m,m)
    exit()
if M*a<=k<=M*b:
    if (k-m*b)%(m*(b-a)):
        m+=1+(k-m*b)//(m*(b-a))
    print(m,M-(k-M*a)//(M*(b-a)))
else:
    print("UNSATISFIABLE")