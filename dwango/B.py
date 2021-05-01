#!/usr/bin/python3
s=list(input())
flag,ans,cnt=0,0,0
search="2"
flag=0
for i in s:
    if search==i:
        if flag:
            cnt+=1
            search=["5" if i=="2" else "2"][0]
        else:
            search="5"
            cnt=1
            flag=1
    else:
        ans+=(cnt//2)*(cnt//2+1)//2
        if i=="2":
            cnt=1
            flag=1
            search="5"
        else:
            cnt=0
            flag=0
            search="2"
print(ans+(cnt//2)*(cnt//2+1)//2)