#!/usr/bin/python3

S=input()
a={chr(i):0 for i in range(97,97+26)}
for i in S:
    a[i]+=1

odd,even=0,0
for i in a:
    odd+=a[i]%2
    even+=a[i]//2
if not odd:
    print(even*2)
else:
    print(2*(even//odd)+1)