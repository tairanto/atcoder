#!/usr/bin/python3

X,Y=map(int,input().split("."))
if Y<=2:
    print(X,"-",sep="")
elif Y<=6:
    print(X,sep="")
else:
    print(X,"+",sep="")