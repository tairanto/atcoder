#!/usr/bin/python3

def hw(l):
    count=l[0][0]-1
    l[0][2]=count
    for i in range(1,len(l)):
        count+=l[i][0]-l[i-1][0]-1+(l[i][0]==l[i-1][0])
        l[i][2]=count
    return l

H,W,N=map(int,input().split())
X,Y=[],[]
for i in range(N):
    a,b=map(int,input().split())
    X.append([a,i+1,0])
    Y.append([b,i+1,0])
X.sort()
Y.sort()
X,Y=hw(X),hw(Y)
X.sort(key=lambda x:x[1])
Y.sort(key=lambda x:x[1])
for i in range(N):
    print(X[i][0]-X[i][2],Y[i][0]-Y[i][2])