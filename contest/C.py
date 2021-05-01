#!/usr/bin/python3
a,b=map(int,input().split())
for i in range(1,b-a+1):
    yakusuu=b//i
    if i*yakusuu<=b and i*(yakusuu-1)>=a:
        ans=i
print(ans)