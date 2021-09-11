#!/usr/bin/python3

def group(seq1,seq2):
    n1,n2=len(seq1[0]),len(seq2)
    s1=len(seq1)
    g1=[]
    for i in range(n1):
        temp={"A":0,"T":0,"G":0,"C":0,"-":0,"all":s1}
        for j in seq1:
            temp[j[i]]+=1
        temp["all"]-=temp["-"]
        g1.append(temp)
    s=[0 for i in range(n2+1)]
    d=[["y" for _ in range(n2+1)]]
    d[0][0]="s"
    for i in range(n1):
        temp=[-g1[i]["all"]*(i+1)]
        direct=["t"]
        for j in range(n2):
            tate=s[j+1]-g1[i]["all"]
            yoko=temp[j]-1
            nana=s[j]+g1[i][seq2[j]]*2
            temp.append(max(tate,yoko,nana))
            direct.append([["y","t"][tate>=yoko],"n"][nana>=max(tate,yoko)])
        s=temp
        d.append(direct)
    aln1,aln2=["" for x in range(s1)],""
    while d[i+1][j+1]!="s":
        if d[i+1][j+1]=="n":
            for x in range(s1):
                aln1[x]=seq1[x][i]+aln1[x]
            aln2=seq2[j]+aln2
            i-=1
            j-=1
        elif d[i+1][j+1]=="t":
            for x in range(s1):
                aln1[x]=seq1[x][i]+aln1[x]
            aln2="-"+aln2
            i-=1
        else:
            for x in range(s1):
                aln1[x]="-"+aln1[x]
            aln2=seq2[j]+aln2
            j-=1
    aln1.append(aln2)
    return aln1

N=int(input())
seq=sorted([[list(input()),i] for i in range(N)],key=lambda x:len(x[0]),reverse=True)
score=float("inf")
ans=0
for x in range(N):
    S=group([seq[0][0]],seq[-x-1][0])
    for i in range(1,N):
        if i==N-x-1:continue
        S=group(S,seq[i][0])
    aaa=0
    for i in range(len(S[0])):
        temp={"A":0,"T":0,"G":0,"C":0,"-":0}
        for j in S:
            temp[j[i]]+=1
        aaa+=N-max(temp.values())
    if score>aaa:
        score=aaa
        ans=S
        num=x
    print(aaa)
# A=[[seq[0][1],ans[0]],[seq[-1-num][1],ans[1]]]
# for i in range(1,N):
#     if i==N-num-1:
#         continue
#     elif i<N-num-1:
#         A.append([seq[i][1],ans[i+1]])
#     else:
#         A.append([seq[i][1],ans[i]])
# A.sort()
# for i in A:
#     print(i[1])