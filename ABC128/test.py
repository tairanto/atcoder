#!/usr/bin/python3
n,k=map(int,input().split())
x=list(map(int,input().split()))
ans=0
for l in range(k+1):
    for r in range(k-l+1):
        if l+r>n:continue
        amari=k-l-r
        temp=[]
        cnt=0
        flag=1
        for i in range(l):
            if flag and x[l-1-i]<0:
                cnt+=1
                continue
            temp.append(x[l-1-i])
            flag=0
        flag=1
        for i in range(r):
            if flag and x[n-r+i]<0:
                cnt+=1
                continue
            temp.append(x[n-r+i])
            flag=0
        temp.sort()
        flag=0
        for i in range(amari):
            if i>=r+l-cnt:
                flag=1
                break
            if temp[i]>0:
                flag=2
                break
        if flag==2:
            ans=max(ans,sum(temp[i:]))
        elif flag==1:
            if (amari-(r+l-cnt))%2 and l+r-cnt>0:
                ans=max(ans,temp[-1])
            else:
                ans=max(ans,0)
        else:
            ans=max(ans,sum(temp[amari:]))
print(ans)
