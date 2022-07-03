#!/usr/bin/python3

N=int(input())
ans=[]
for i in range(1<<N):
    flag=0
    for j in range(N):
        if flag==(i>>j)%2==0:
            flag=-1
            break
        else:
            if (i>>j)%2:
                flag+=1
            else:
                flag-=1
    if flag:continue
    ans.append("".join(["(" if (i>>j)%2 else ")" for j in range(N)]))
print(*sorted(ans),sep="\n")