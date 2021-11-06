#!/usr/bin/python3


N=int(input())
for i in range(N):
    t1,t2,t3=map(int,input().split())
    ans=0
    N2=t2//2
    if t3-N2>=0:
        ans+=N2
        t3-=N2
        N2=0
    else:
        ans+=t3
        N2-=t3
        t3=0
    if t1//2-N2>=0:
        ans+=N2
        t1-=N2*2
        N2=0
    else:
        ans+=t1//2
        N2-=t1//2
        t1%=2
    if t1-t3//2>=0:
        ans+=t3//2
        t1-=t3//2
        t3%=2
    else:
        ans+=t1
        t3-=t1*2
        t1=0
    if t1//3-t3>=0:
        ans+=t3
        t1-=t3*3
        t3=0
    else:
        ans+=t1//3
        t3-=t1
        t1=0
    ans+=t1//5
    print(ans)