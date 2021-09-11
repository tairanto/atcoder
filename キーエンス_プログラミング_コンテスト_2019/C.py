#!/usr/bin/python3

N=int(input())
a,b=list(map(int,input().split())),list(map(int,input().split()))
if sum(a)<sum(b):
    print(-1)
    exit()
diff=[a[i]-b[i] for i in range(N)]
diff.sort()
cnt,i,j=0,0,0
while diff[i]<0:
    if diff[-1-j]+diff[i]>=0:
        diff[-1-j]+=diff[i]
        i+=1
    else:
        diff[i]+=diff[-1-j]
        j+=1
    cnt+=1
print(cnt+(cnt>0))