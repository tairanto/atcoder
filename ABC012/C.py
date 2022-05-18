N=int(input())
for i in range(1,10):
    if (2025-N)%i==0 and (2025-N)//i<10:
        print(i,"x",(2025-N)//i)