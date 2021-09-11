#!/usr/bin/python3


h,w,K=map(int,input().split())
grid=[list(input()) for i in range(h)]
ans=0
for i in range(1<<h):
    for j in range(1<<w):
        temp=[[grid[j][i] for i in range(w)]for j in range(h)]
        for bit in range(h):
            if (i>>bit)%2:
                for k in range(w):
                    temp[bit][k]="R"
        for bit in range(w):
            if (j>>bit)%2:
                for k in range(h):
                    temp[k][bit]="R"
        if K==sum([temp[k].count("#") for k in range(h)]):
            ans+=1
print(ans)