"""
Q.
0からNまでの整数の数を出力せよ
ただし、N≦1000000とする

"""
# Input
N_str = input()
len_N = len(N_str)
N_int = int(N_str)


def update(digit_num, is_max):
    global N_str

    num_int_max0, num_int_max1 = -1, -1
    if is_max == 1:
        num_int_max0 = digit_num
        num_int_max1 = 1
    else:
        num_int_max0 = 10
    return num_int_max0, num_int_max1


# Initial DP settings
dp = [[-1, -1] for _ in range(len_N)]
dp[0][0] = int(N_str[0])
dp[0][1] = 1

# DP calculations
for i, dpv in enumerate(dp[:-1]):
    next_digit_num = int(N_str[i + 1])
    num_int_max0_frm1, num_int_max1_frm1 = update(next_digit_num, 1)
    num_int_max0_frm0, _ = update(next_digit_num, 0)

    dp[i + 1][0] = num_int_max0_frm0 * dp[i][0] + num_int_max0_frm1 * dp[i][1]
    dp[i + 1][1] = num_int_max1_frm1 * dp[i][1]

# Result
print(dp[-1][0] + dp[-1][1])
