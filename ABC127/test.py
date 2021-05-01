#!/usr/bin/python3
n,m=map(int,input().split())
x=list(map(int,input().split()))
ans={}
for i in x:
    if not i in ans.keys():
        ans[i]=0
    ans[i]+=1
for i in range(m):
    b,c=map(int,input().split())
    if not c in ans.keys():
        ans[c]=0
    ans[c]+=b
key=list(ans.keys())
key.sort()
cnt=0
for i in range(len(key)):
    if ans[key[-1-i]]<=n:
        n-=ans[key[-1-i]]
        cnt+=ans[key[-1-i]]*key[-1-i]
    else:
        cnt+=n*key[-1-i]
        break
print(cnt)