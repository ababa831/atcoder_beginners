# WIP
N, K = map(int, input().split())
hhh = list(map(int, input().split()))

dp = [0] * N
dp[0] = 0
dp[1] = abs(hhh[1] - hhh[0])
dp[2] = abs(hhh[2] - hhh[1]) + abs(hhh[1] - hhh[0]) + abs(hhh[2]-hhh[0])