#!/usr/bin/python3
n=int(input())
a,b=list(map(int,input().split())),list(map(int,input().split()))
i,cnt,ans=0,0,0
while cnt<n:
    if a[i]<=b[cnt]:
        b[cnt]-=a[i]
        ans+=a[i]
        if abs(i-cnt)==1:
            cnt+=1
        i+=1
    else:
        a[i]-=b[cnt]
        ans+=b[cnt]
        if i==cnt:
            i+=1
        cnt+=1
print(ans)