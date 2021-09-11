#!/usr/bin/python3

a,b,c=map(int,input().split())
for i in range(max(a,b)):
    if a*(i+1)%b==c:
        print("YES")
        exit()
print("NO")