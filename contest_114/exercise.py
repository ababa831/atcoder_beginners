# WIP
"""
# http://tutuz.hateblo.jp/entry/2018/06/16/150252

Q.
0からNまでの整数のうち、5を使用しない整数の数を求めよ
ただし、N≦1000000とする

A.
https://densanken.com/wiki/index.php?%B7%E5DP
"""

N_str = input()
len_N = len(N_str)
N = int(N_str)

dp = [[-1, -1] for _ in range(len_N)]  # dp[digit][smaller]

# Initial settings
digit_num = N_str[0]
if digit_num > 5:
    # X, 6, ..., 4, 3, 2, 1
    dp[0][0] = 1
    dp[0][1] = digit_num - 2
elif digit_num == 5:
    dp[0][0] = 0
    dp[0][1] = 4
else:
    dp[0][0] = 1
    dp[0][1] = digit_num - 1

for i in range(len_N):
    digit_num = N_str[i]
    if digit_num > 5:
        # X, 6, ..., 4, 3, 2, 1, "0"
        dp[i+1][0] = 1 * dp[i][0]
        dp[i+1][1] = (digit_num - 2) * dp[i][0] + 10 * dp[i][1]
    elif digit_num == 5:
        dp[i+1][0] = 0
        dp[i+1][1] = 4



