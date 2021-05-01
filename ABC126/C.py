#!/usr/bin/python3
n,k=map(int,input().split())
ans=0
bit=[2**(i+1) for i in range(17)]
# print(bit)
for i in range(1,n+1):
    p=0
    if i<k:
        for x,j in enumerate(bit):
            if j*i>=k:
                p=x+1
                break
    ans+=(1/n)/pow(2,p)
print(ans)