# AC
# https://atcoder.jp/contests/dp/tasks/dp_a
N = int(input())
hhh = list(map(int, input().split()))

dp = [0] * N
dp[0] = 0
dp[1] = abs(hhh[1] - hhh[0])

for i in range(2, N):
    dp[i] = min(
        abs(hhh[i] - hhh[i - 1]) + dp[i - 1],
        abs(hhh[i] - hhh[i - 2]) + dp[i - 2])

print(dp[N - 1])
