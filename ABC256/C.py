#!/usr/bin/python3

h1,h2,h3,w1,w2,w3=map(int,input().split())
ans=0
for i in range(1,29):
    for j in range(1,29):
        for k in range(1,29):
            for l in range(1,29):
                if h1-i-j>0 and h2-k-l>0 and w1-i-k>0 and w2-j-l>0 and w3-(h1+h2)+(i+j+k+l)>0 and w3-(h1+h2)+(i+j+k+l)==h3-(w1+w2)+(i+j+k+l):
                    ans+=1
print(ans)