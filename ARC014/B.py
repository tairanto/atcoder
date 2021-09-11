#!/usr/bin/python3

n=int(input())
s=set()
for i in range(n):
    if i==0:
        now=input()
        s.add(now)
    else:
        temp=input()
        if temp in s or now[-1]!=temp[0]:
            if i%2:
                print("WIN")
            else:
                print("LOSE")
            exit()
        else:
            s.add(temp)
            now=temp
print("DRAW")