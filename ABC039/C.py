#!/usr/bin/python3


s=list(input())
x=[]
ans=["Do","Do","Re","Re","Mi","Fa","Fa","So","So","La","La","Si"]
for i in range(19):
    if s[i]==s[i+1]:
        x.append(i)
    if len(x)==2:
        break
if x[1]-x[0]==5:
    print(ans[-1-x[0]])
else:
    print(ans[4-x[0]])