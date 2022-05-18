def keta(temp):
    ans=[1,0]
    for i,x in enumerate(temp):
        num=int(x)
        ans[1]=ans[0]*(num-(num>=4)+(num==4))+ans[1]*8
        if ans[0]:ans[0]=[1,0][num==4 or num==9]
    return ans[1]+(not "4" in temp and not "9" in temp)

A,B=input().split()
A=str(int(A)-1)
print(-int(A)+int(B)-keta(B)+keta(A))