"""
# http://tutuz.hateblo.jp/entry/2018/06/16/150252

Q.
0からNまでの整数のうち、5を使用しない整数の数を求めよ
ただし、N≦1000000とする

A.
https://densanken.com/wiki/index.php?%B7%E5DP
"""
"""WA
N = input()
len_N = len(N)
N = int(N)

dp = [0] * (len_N+1)
dp[0] = 0
dp[1] = 9  # 0~4, 6~9

for d in range(2, len_N+1):
    num_wo_5 = 8
    dp[d] = num_wo_5 * dp[d-1] + dp[d-2]
    print(dp[d])

print(dp[len_N-1]+1)
"""
