num=input()
z=[bin(i)[3:] for i in range(8,16)]
for i in z:
    total=int(num[0])
    s=""
    for x,j in enumerate(list(i)):
        if j=="0":
            total+=int(num[1+x])
            s+="+"
        else:
            total-=int(num[1+x])
            s+="-"
    if total==7:
        print(num[0]+s[0]+num[1]+s[1]+num[2]+s[2]+num[3]+"=7")
        exit()