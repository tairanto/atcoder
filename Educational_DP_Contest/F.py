#!/usr/bin/python3


s1,s2=input(),input()
dp=[[0 for _ in range(len(s2)+1)]for _ in range(len(s1)+1)]
ans=[["y" for _ in range(len(s2)+1)]]
for i in range(len(s1)):
    temp=["t"]
    for j in range(len(s2)):
        t,y,n=dp[i][j+1],dp[i+1][j],dp[i][j]+(s1[i]==s2[j])
        dp[i+1][j+1]=max(t,y,n)
        temp.append([["y","t"][t>y],"n"][n>max(t,y)])
    ans.append(temp)
lcs=""
while i>-1 and j>-1:
    if ans[i+1][j+1]=="n":
        lcs+=s1[i]
        i-=1
        j-=1
    elif ans[i+1][j+1]=="y":
        j-=1
    else:
        i-=1
print(*reversed(lcs),sep="")