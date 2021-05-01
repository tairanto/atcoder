#!/usr/bin/python3
a,b,c=list(input()),list(input()),list(input())
S_all=list(set(a+b+c))
n=len(S_all)
import itertools
l = [str(i) for i in range(1,10)]+["0"]
p = itertools.permutations(l, n)
flag=1
for i in p:
    s={S_all[j]:i[j] for j in range(n)}
    n1,n2,n3="","",""
    for j in a:
        n1+=s[j]
    for j in b:
        n2+=s[j]
    for j in c:
        n3+=s[j]
    if n1[0]=="0" or n2[0]=="0" or n3[0]=="0":continue
    if int(n1)+int(n2)==int(n3):
        print(n1,n2,n3,sep="\n")
        flag=0
        break
if flag:print("UNSOLVABLE")