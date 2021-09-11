#!/usr/bin/python3


n=int(input())
#最後に残ったものの計算のために[0]
x=list(map(int,input().split()))+[0]
c=[-1]#全部が最小値を持つ場合の計算
ans=0
for i in range(n+1):
    #今の位置-1からappendした位置-1([-1除く])まで（i-c[-2]-1）とその時の数値x[c[-1]]の最大
    while x[c[-1]]>x[i]:
        ans=max(ans,(i-c[-2]-1)*x[c[-1]])
        c.pop()
    c.append(i)
print(ans)