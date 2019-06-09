import sys

N, M = map(int, input().split())

if M == 0:
    alist = set()
else:
    # Input below rows
    alist = set(map(int, sys.stdin))

dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1 if 1 not in alist else 0

MOD = 10**9 + 7
for i in range(2, N + 1):
    if i in alist:
        continue
    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

print(dp[N])
