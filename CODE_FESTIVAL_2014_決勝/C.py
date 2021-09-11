#!/usr/bin/python3

def F(k,ans):
    temp=list(str(k))
    total=0
    for i in range(len(temp)):
        total+=pow(k,i)*int(temp[-1-i])
        if total>ans:
            return False
    if total==ans:
        return True
    return False

n=int(input())
for i in range(10,10**4+1):
    if F(i,n):
        print(i)
        exit()
print(-1)