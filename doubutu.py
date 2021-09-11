#!/usr/bin/python3

def weight(l,a,b,T):
    temp={}
    for i in l:
        if not i-a in temp:
            temp[i-a]=0
        temp[i-a]+=l[i]
        if i+b>T:continue
        if not i+b in temp:
            temp[i+b]=0
        temp[i+b]+=l[i]
    return temp

N,S,T=map(int,input().split())
count=0
W={S:1}
for i in range(min(count,N)):
    A,B=map(int,input().split())
    W=weight(W,A,B,T)

def hanbun(l,a,b,n):
    temp={}
    for i in l:
        if not i-a in temp:
            temp[i-a]=-float("inf")
        temp[i-a]=max(1<<(N-count-n-1),temp[i-a])
        if not i+b in temp:
            temp[i+b]=-float("inf")
        temp[i+b]=max(1<<(N-count-n-1),temp[i+b])
    return temp

H={0:0}
ori={}
for i in range(max(0,N-count)):
    A,B=map(int,input().split())
    H=hanbun(H,A,B,i)
    for i in H:
        if not i in ori:
            ori[i]=-float("inf")
        ori[i]=max(ori[i],H[i])
print(ori)
print(1<<N,sum([ori[i] for i in sorted(ori.keys()) if i >10]))