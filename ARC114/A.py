#!/usr/bin/python3
sosuu=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
n=int(input())
x=list(map(int,input().split()))
bit=[0 for i in range(n)]
for cnt1,i in enumerate(x):
    for cnt2,j in enumerate(sosuu):
        if i%j==0:
            bit[cnt1]|=1 << cnt2
ans=2
for i in sosuu:ans*=i
for i in range(1<<len(sosuu)):
    flag=0
    for j in bit:
        if (j & i)==0:
            flag=1
            break
    if flag:continue
    temp=1
    for j in range(len(sosuu)):
        if (i >> j)%2==1:temp*=sosuu[j]
    ans = min(ans,temp)
print(ans)