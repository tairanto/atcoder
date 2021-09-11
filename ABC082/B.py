#!/usr/bin/python3

s,t=list(input()),list(input())
s.sort()
t.sort(reverse=True)
ans=["".join(s),"".join(t)]
ans.sort(key=len)
ans.sort()
if ans[0]==ans[1] or ans[1]!="".join(t):
    print("No")
else:
    print("Yes")
    