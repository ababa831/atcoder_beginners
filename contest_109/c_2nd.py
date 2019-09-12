# AC
import sys
from fractions import gcd

sys_input = sys.stdin.readline

N, X = map(int, sys_input().split())
xxx = list(map(int, sys_input().split()))
xxx = list(map(lambda x: abs(x-X), xxx))

dp = [None] * N
dp[0] = xxx[0]

for i, x in enumerate(xxx):
    if i == 0:
        continue
    dp[i] = gcd(dp[i-1], x)

print(dp[N-1])
