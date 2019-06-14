# Python3  -> TLE
# PyPy3 -> AC
N, K = map(int, input().split())
hhh = list(map(int, input().split()))

dp = [0] * N
dp[0] = 0

for i in range(1, N):
    if i < K:
        dp[i] = \
            min([abs(hhh[i] - hhh[i-k]) + dp[i-k] for k in range(1, i+1)])
    else:
        dp[i] = \
            min([abs(hhh[i] - hhh[i-k]) + dp[i-k] for k in range(1, K+1)])

print(dp[-1])
