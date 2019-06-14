# Python3
N, K = map(int, input().split())
hhh = list(map(int, input().split()))

dp = [0] * N
dp[0] = 0

for i, h in enumerate(hhh):
    s = 0 if i < K else i-K
    if i == 0:
        continue
    dp[i] = \
        min([abs(h - h_k) + dp_k for h_k, dp_k in zip(hhh[s:i], dp[s:i])])

print(dp[-1])
