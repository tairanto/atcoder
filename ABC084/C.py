#!/usr/bin/python3

N=int(input())
station=[[*map(int,input().split())] for i in range(N-1)]
for i in range(N-1):
    ans=station[i][0]+station[i][1]
    for j in range(i+1,N-1):
        if ans<=station[j][1]:
            ans=station[j][1]
        else:
            ans=ans+(station[j][2]-(ans-station[j][1])%station[j][2])%station[j][2]
        ans+=station[j][0]
    print(ans)
print(0)
