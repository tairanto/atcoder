#!/usr/bin/python3



N,A,B,C,D=map(int,input().split())
S=list(input())
nuku=C>D
A,B,C,D=A-1,B-1,C-1,D-1
while A!=C:
    if nuku:
        if B-1<=A and A+2<=D+1 and S[A:A+3]==[".",".","."]:
            nuku=0
    if S[A+1]==".":
        A+=1
    elif A+2<=C and S[A+2]==".":
        A+=2
    else:
        print("No")
        exit()
while B!=D: 
    if S[B+1]==".":
        B+=1
    elif B+2<=D and S[B+2]==".":
        B+=2
    else:
        print("No")
        exit()
if nuku:
    print("No")
else:
    print("Yes")