#!/usr/bin/python3

a,k=map(int,input().split())
ans=0
if k==0:
    print(2*(10**12)-a)
    exit()
while a<2*(10**12):
    a=1+(1+k)*a
    ans+=1
print(ans)