# AC
from fractions import gcd

N = int(input())
AAA = list(map(int, input().split()))

dp = [0] * (N + 1)
dp[0] = AAA[0]

for i, A in enumerate(AAA):
    if i == N:
        break
    dp[i + 1] = gcd(dp[i], A)

print(dp[N])
