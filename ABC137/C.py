#!/usr/bin/python3


n=int(input())
ans={}
for i in range(n):
    temp=list(input())
    temp.sort()
    temp="".join(temp)
    if not temp in ans.keys():
        ans[temp]=0
    ans[temp]+=1
print(sum([ans[i]*(ans[i]-1)//2 for i in ans]))