#!/usr/bin/python3
n,s=input().split()
n=int(n)
atgc=[[0,0,0,0]]#ATGC
for i in s:
    atgc.append([atgc[-1][0]+(i=="A"),atgc[-1][1]+(i=="T"),
    atgc[-1][2]+(i=="G"),atgc[-1][3]+(i=="C")])
cnt=0
l=2
while l<=n:
    for i in range(n-l+1):
        if atgc[l+i][0]-atgc[i][0]!=atgc[l+i][1]-atgc[i][1]:continue
        if atgc[l+i][2]-atgc[i][2]!=atgc[l+i][3]-atgc[i][3]:continue
        cnt+=1
    l+=2
print(cnt)