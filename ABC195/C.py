#!/usr/bin/python3
N=input()
x=len(N)
n3=999
n6=int("9"*6)-n3
n9=(int("9"*9)-int("9"*6))*2+n6
n12=(int("9"*12)-int("9"*9))*3+n9
if x<4:
    print(0)
elif x<7:
    print(int(N)-n3)
elif x<10:
    print((int(N)-int("9"*6))*2+n6)
elif x<13:
    print((int(N)-int("9"*9))*3+n9)
elif x<16:
    print((int(N)-int("9"*12))*4+n12)
else:
    print((int("9"*15)-int("9"*12))*4+n12+5)