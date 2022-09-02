#!/usr/bin/python3

N=int(input())
T=[*map(int,input().split())]
now=0
for i in T:
    baisuu=1<<i
    if baisuu>now:
        now=baisuu
    else:
        now=((now//baisuu)+1)*baisuu
        if now%(baisuu*2)==0:
            now+=baisuu
print(now)

# 1
# # 0 0 0 0 1

# 1 1
# # 0 0 0 1 0
# # 0 0 0 1 1

# 2 1 1
# # 0 0 1 0 0
# # 0 0 1 0 1
# # 0 0 1 1 0
# # 0 0 1 1 1

# 4 2 1 1
# # 0 1 0 0 0
# # 0 1 0 0 1
# # 0 1 0 1 0
# # 0 1 0 1 1
# # 0 1 1 0 0

# # 0 1 1 0 1
# # 0 1 1 1 0
# # 0 1 1 1 1
