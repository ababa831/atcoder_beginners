# WIP
from itertools import product

N_str = input()
len_N = len(N_str)
N = int(N_str)

# DP Initialization
dp = [[[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)]
       for _ in range(2)] for _ in range(len_N)]
# dp[digit][is_max][is_3][is_5][is_7]

"""
for l in range(len_N):
    dp[l][0][0][0][0] = 1
"""


# DP at 0 digit
for m in range(10):
    digit_0 = int(N_str[0])
    if m > digit_0:
        continue
    if digit_0 in [3, 5, 7]:
        dp[0][digit_0 == m][m == 3][m == 5][m == 7] = 1


for l, m, n, o, p in product(range(len_N - 1), range(10), range(2), range(2),
                             range(2)):
    if m in [3, 5, 7]:
        digit_lp1 = int(N_str[l + 1])
        dp[l+1][0][n or m == 3][o or m == 5][p or m == 7] += \
            dp[l][0][n][o][p]

        if digit_lp1 < m:
            continue

        dp[l+1][digit_lp1 == m][n or m == 3][o or m == 5][p or m == 7] += \
            dp[l][1][n][o][p]

print(dp[-1][0][1][1][1] + dp[-1][1][1][1][1])
