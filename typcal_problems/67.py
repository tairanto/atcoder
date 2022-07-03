#!/usr/bin/python3

def etn(n):
    ten,nine=0,0
    for x,i in enumerate(reversed(n)):
        ten+=int(i)*(8**x)
    ans=[]
    for i in range(20,-1,-1):
        num=ten//(9**i)
        if num==8:
            ans.append("5")
        else:
            ans.append(str(num))
        ten-=(9**i)*num
    return ans

N,K=input().split()
N=list(N)
for i in range(int(K)):
    N=etn(N)
print(int("".join(N)))