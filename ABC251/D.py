#!/usr/bin/python3

W=int(input())
ans=[]
for i in range(1,100):
    ans.extend((i,100*i,10000*i))
print(len(ans))
print(*ans)