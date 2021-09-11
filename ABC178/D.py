#!/usr/bin/python3

MAX = 510000
MOD = 1000000007

fac,finv,inv=[1,1],[1,1],[0,1]

# テーブルを作る前処理
def COMinit():
    for i in range(2,MAX):
        fac.append(fac[i - 1] * i % MOD)
        inv.append(MOD - inv[MOD%i] * (MOD // i) % MOD)
        finv.append(finv[i - 1] * inv[i] % MOD)

# 二項係数計算
def COM(n,k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    # print(fac[n] ,finv[k] , finv[n - k])
    return (fac[n] * (finv[k] * finv[n - k] % MOD) % MOD)


# 前処理
COMinit()

S=int(input())
ans=0
for i in range(1,S//3+1):
  ans+=COM(S-3*i+i-1,i-1)
print(ans%MOD)