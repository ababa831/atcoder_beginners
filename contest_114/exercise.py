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

dp = [[-1, -1] for _ in range(len_N)]  # dp[digit][is_max]


def update(digit, is_max):
    num_next, num_next_0, num_next_1 = None, None, None
    if is_max == 0:
        num_next = 9
        is_max_next = 0
        return num_next, is_max_next
    else:
        if digit > 5:
            num_next_0 = digit-1
            num_next_1 = 1
        else:
            num_next_0 = digit
            num_next_1 = 1
        is_max_next_0, is_max_next_1 = 0, 1
        return num_next_0, is_max_next_0, num_next_1, is_max_next_1


digit_0 = int(N_str[0])
dp[0][0] = digit_0-1 if digit_0 > 5 else digit_0
dp[0][1] = 1

for i, dp_v in enumerate(dp[:-1]):
    digit = int(N_str[i])
    num_next_0_frm0, is_max_next_0_frm0 = update(digit, 0)
    num_next_0_frm1, is_max_next_0_frm1, num_next_1, is_max_next_1 = \
        update(digit, 1)

    print(dp_v)
    dp[i+1][1] = num_next_1 * dp_v[1]
    dp[i+1][0] = num_next_0_frm0 * dp_v[0] + num_next_0_frm1 * dp_v[1]

# Show result
print(dp[-1][0] + dp[-1][1])
