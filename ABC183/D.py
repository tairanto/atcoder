#!/usr/bin/python3

N,W=map(int,input().split())
st=[0 for i in range(2*10**5+1)]
for i in range(N):
    s,t,w=map(int,input().split())
    st[s]+=w
    st[t]-=w
now=0
for i in st:
    now+=i
    if now>W:
        print("No")
        exit()
print("Yes")