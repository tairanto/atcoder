#!/usr/bin/python3
s=input()
d={}
for i in list(s):
    if not i in d:
        d[i]=0
    d[i]+=1
if len(d)==2 and d[list(d.keys())[0]]==d[list(d.keys())[0]]:
    print("Yes")
else:
    print("No")