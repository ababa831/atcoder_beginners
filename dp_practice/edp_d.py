# PyPy3 -> AC
N, W = map(int, input().split())

dp = [[0] * (W+1) for _ in range(N+1)]

for i in range(1, N+1):
    w, v = map(int, input().split())
    for w_k in range(1, W+1):
        if w_k >= w:
            dp[i][w_k] = max(dp[i-1][w_k-w] + v, dp[i-1][w_k])
        else:
            dp[i][w_k] = dp[i-1][w_k]

print(max(dp[N]))
