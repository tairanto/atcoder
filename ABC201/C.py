#!/usr/bin/python3
key=list(input())
o,humei=[],[]
for i in range(10):
    if key[i]=="o":o.append(i)
    elif key[i]=="?":humei.append(i)
lo,lh=len(o),len(humei)
if lo==4:
    print(24)
elif lo==3 and lh>0:
    print(24*lh+12*3)
elif lo==2 and lh>0:
    print(24*lh+14+12*lh*lh)
elif lo==1 and lh>0:
    print(1+4*lh+6*(lh**2)+4*(lh**3))
elif lo==0 and lh>0:
    print(lh**4)
else:
    print(0)
