#!/usr/bin/python3

S=input()
ans=0
for i in range(1<<(len(S)-1)):
    temp=S[0]
    for j in range(len(S)-1):
        if (i>>j)%2:
            ans+=int("".join(temp))
            temp=S[1+j]
        else:
            temp+=S[1+j]
    ans+=int("".join(temp))
print(ans)