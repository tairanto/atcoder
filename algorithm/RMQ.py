#!/usr/bin/python3

#pypyの方が速かった

from sys import setrecursionlimit
setrecursionlimit(10**9)
class SegmentTree:
    def __init__(self,N) -> None:
        self.size=1
        while self.size<N:self.size*=2
        self.dat=[0]*self.size*2

    def update(self,pos,x) -> None:
        pos = pos+self.size-1
        self.dat[pos]=x
        while pos>1:
            pos//=2
            self.dat[pos]=max(self.dat[pos*2],self.dat[pos*2+1])
    
    def get(self,l,r,a,b,u) -> int:#[l,r)がクエリの区間全域,[a,b)が今見ている区間,uがdatのindex
        if r<=a or b<=l:return -INF
        if l<=a and b<=r:return self.dat[u]
        m=(a+b)//2
        AnsL=seg.get(l,r,a,m,u*2)
        AnsR=seg.get(l,r,m,b,u*2+1)
        return max(AnsL,AnsR)
        
INF=float("INF")
N,Q=map(int,input().split())
seg=SegmentTree(N)
for i in range(Q):
    q,a,b=map(int,input().split())
    if q-1:
        print(seg.get(a,b,1,seg.size+1,1))
    else:
        seg.update(a,b)

