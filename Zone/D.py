#!/usr/bin/python3
s=list(input())
R=0
s1,s2=[],[]
for i in s:
    if i=="R":
        R+=1
        continue
    if R%2:
        s2.append(i)
    else:
        s1.append(i)
if R%2==0:
    s2.reverse()
    S=s2+s1
else:
    s1.reverse()
    S=s1+s2

flag=0
ans=["R"]
cnt=0
while cnt<len(S):
    if ans[-1]==S[cnt]:
        ans.pop(-1)
    else:
        ans.append(S[cnt])
    cnt+=1
print(*ans[1:],sep="")