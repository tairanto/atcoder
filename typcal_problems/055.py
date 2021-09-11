#!/usr/bin/python3

def ka(a,b,c,d,e):
    temp=a*b%P
    temp=temp*c%P
    temp=temp*d%P
    temp=temp*e%P
    return temp

N,P,Q=map(int,input().split())
A=list(map(int,input().split()))
ans=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            for l in range(k+1,N):
                for m in range(l+1,N):
                    if ka(A[i],A[j],A[k],A[l],A[m])==Q:ans+=1
print(ans)