#!/usr/bin/python3
def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)

a,b=map(int,input().split())
n=GCD(a,b)
if n==1:
    print(1)
    exit()
N=[]
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        N+=[i,n//i]
cnt=0
for i in N:
    flag=1
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            flag=0
            break
    if flag:
        cnt+=1
print(cnt)