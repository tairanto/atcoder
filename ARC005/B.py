#!/usr/bin/python3

x,y,w=input().split()
grid=[list(map(int,input())) for i in range(9)]
y,x,w=int(x)-1,int(y)-1,list(w)
ans=[grid[x][y]]
for i in range(3):
    if "R" in w:y+=1
    elif "L" in w:y-=1
    if "U" in w:x-=1
    elif "D" in w:x+=1
    if x<0:
        x=1
        w[w.index("U")]="D"
    elif x>8:
        x=7
        w[w.index("D")]="U"
    if y<0:
        y=1
        w[w.index("L")]="R"
    elif y>8:
        y=7
        w[w.index("R")]="L"
    ans.append(grid[x][y])
print(*ans,sep="")
    