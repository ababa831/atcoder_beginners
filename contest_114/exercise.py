# OK
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

dp = [[-1, -1] for _ in range(len_N)]  # "is_max" in the list

# i == 0
d_0 = int(N_str[0])
if d_0 > 5:
    dp[0][0] = d_0 - 1
    dp[0][1] = 1
elif d_0 == 5:
    dp[0][0] = d_0
    dp[0][1] = 0
else:
    dp[0][0] = d_0
    dp[0][1] = 1

for i, dpv in enumerate(dp[:-1]):
    next_d = int(N_str[i + 1])
    if next_d > 5:
        next_ismax0 = next_d - 1
        next_ismax1 = 1
    elif next_d == 5:
        next_ismax0 = next_d
        next_ismax1 = 0
    else:
        next_ismax0 = next_d
        next_ismax1 = 1

    dp[i + 1][0] = dp[i][0] * 9 + dp[i][1] * next_ismax0
    dp[i + 1][1] = dp[i][1] * next_ismax1

print(dp[-1][0] + dp[-1][1])
