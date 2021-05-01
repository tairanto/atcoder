#!/usr/bin/python3
n,c,k=map(int,input().split())
t=[int(input()) for _ in range(n)]
t.sort()
cnt,ans=0,0
if c==1:
    print(n)
    exit()
for i in t:
    if cnt==0:
        st=i
        cnt+=1
    else:
        if i-st<=k:
            if cnt==c-1:
                ans+=1
                cnt=0
            else:
                cnt+=1
        else:
            ans+=1
            cnt=1
            st=i
print(ans+[1 if cnt else 0][0])