#!/usr/bin/python3

n=int(input())
s=list(input())
back=n-1
ans=0
for i in range(n):
    if s[i]=="W":
        flag=0
        while back>i:
            if s[back]=="R":
                flag=1
                break
            back-=1
        if flag:
            s[i],s[back]=s[back],s[i]
            ans+=1
        else:
            print(ans)
            exit()
print(ans)