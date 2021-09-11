#!/usr/bin/python3




N=int(input())
x=[*map(int,input().split())]
ans=-float("inf")
for i in range(N):
    score=[]
    temp={}
    for j in range(N):
        if i==j:continue
        takahashi,aoki=0,0
        m,M=min(i,j),max(i,j)+1
        for k in range(m,M):
            if (m-k)%2:
                aoki+=x[k]
            else:
                takahashi+=x[k]
        score.append(aoki)
        if not aoki in temp:
            temp[aoki]=[]
        temp[aoki].append([j,takahashi])
    score.sort()
    ans=max(ans,sorted(temp[score[-1]])[0][1])
print(ans)