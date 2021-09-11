#!/usr/bin/python3

def cal():
    n=set()
    for i in range(2,10**5+1):
        flag=1
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                flag=0
                break
        if flag:n.add(i)
    return n
N=int(input())
sosuu=cal()
c=[0]
for i in range(1,10**5):
    c.append(c[i-1]+(i%2 and i in sosuu and (i+1)//2 in sosuu))
for i in range(N):
    l,r=map(int,input().split())
    print(c[r]-c[l-1])        