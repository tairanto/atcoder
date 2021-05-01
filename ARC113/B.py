#!/usr/bin/python3
a,b,c=input().split()
b,c=int(b),int(c)
if a[-1]=="0" or a[-1]=="1" or a[-1]=="5" or a[-1]=="6":
    print(a[-1])
elif a[-1]=="4" or a[-1]=="9":
    if b%2:
        print(a[-1])
    else:
        if a[-1]=="4":print("6")
        else:print("1")
else:
    if b%4==1:
        print(a[-1])
    elif b%4==2:
        if c==1:
            if a[-1]=="2" or a[-1]=="8":
                print(4)
            else:
                print(9)
        else:
            if a[-1]=="2" or a[-1]=="8":
                print(6)
            else:
                print(1)
    elif b%4==0:
        if a[-1]=="2" or a[-1]=="8":
            print(6)
        else:
            print(1)
    else:
        if c%2==0:
            print(a[-1])
        else:
            if a[-1]=="2":print(8)
            elif a[-1]=="3":print(7)
            elif a[-1]=="7":print(3)
            elif a[-1]=="8":print(2)