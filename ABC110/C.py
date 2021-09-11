#!/usr/bin/python3


S,T=list(input()),list(input())
s={chr(i):"?" for i in range(97,97+26)}
t={chr(i):"?" for i in range(97,97+26)}
for i in range(len(S)):
    if s[S[i]]=="?":
        s[S[i]]=T[i]
    else:
        if s[S[i]]!=T[i]:
            print("No")
            exit()
    if t[T[i]]=="?":
        t[T[i]]=S[i]
    else:
        if t[T[i]]!=S[i]:
            print("No")
            exit()
print("Yes")