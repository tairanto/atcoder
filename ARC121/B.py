#!/usr/bin/python3

def serach(X,index):
    if index==2*10**15:return 2*10**15
    return min(abs(index-X[bisect.bisect(X,index)-1]),abs(index-X[bisect.bisect(X,index)]))

import bisect
N=int(input())
R,G,B=[2*10**15],[2*10**15],[2*10**15]
for i in range(2*N):
    a,c=input().split()
    if c=="R":R.append(int(a))
    elif c=="G":G.append(int(a))
    else:B.append(int(a))
R.sort()
G.sort()
B.sort()
ans=10**16
if len(R)%2-1 and len(G)%2-1:
    ans=min([serach(G,i) for i in R])
    if len(B)>1:ans=min(ans,min([serach(B,i) for i in R])+min([serach(B,i) for i in G]))
elif len(R)%2-1 and len(B)%2-1:
    ans=min([serach(B,i) for i in R])
    if len(G)>1:ans=min(ans,min([serach(G,i) for i in R])+min([serach(G,i) for i in B]))
elif len(G)%2-1 and len(B)%2-1:
    ans=min([serach(B,i) for i in G])
    if len(R)>1:ans=min(ans,min([serach(R,i) for i in B])+min([serach(R,i) for i in G]))
else:
    ans=0
print(ans)