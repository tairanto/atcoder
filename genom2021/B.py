#!/usr/bin/python3


seq1=list(input())
seq2=list(input())
n1,n2=len(seq1),len(seq2)
s=[[0 for _ in range(n2+1)] for _ in range(n1+1)]
d=[[0 for _ in range(n2+1)] for _ in range(n1+1)]
for i in range(1,n1+1):
    s[i][0]=-5*i
    d[i][0]="t"
for j in range(1,n2+1):
    s[0][j]=-5*j
    d[0][j]="y"
d[0][0]="s"
for i in range(n1):
    for j in range(n2):
        tate=s[i][j+1]-5
        yoko=s[i+1][j]-5
        nana=s[i][j]+[1,-3][seq1[i]!=seq2[j]]
        s[i+1][j+1]=max(tate,yoko,nana)
        if nana>max(tate,yoko):
            d[i+1][j+1]="n"
        else:
            if tate>=yoko:
                d[i+1][j+1]="t"
            else:
                d[i+1][j+1]="y"
aln1,aln2="",""
while d[i+1][j+1]!="s":
    if d[i+1][j+1]=="n":
        aln1=seq1[i]+aln1
        aln2=seq2[j]+aln2
        i-=1
        j-=1
    elif d[i+1][j+1]=="t":
        aln1=seq1[i]+aln1
        aln2="-"+aln2
        i-=1
    else:
        aln1="-"+aln1
        aln2=seq2[j]+aln2
        j-=1
print(aln1,aln2,sep="\n")