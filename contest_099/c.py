# WIP
from math import log
N = int(input())
log_N = log(N)


def search_range(target_yen, n):
    x = 1
    log_value = log(target_yen)
    log_n = log(n)
    while log_n > log_value:
        x += 1
        log_value = x * log(target_yen)
    return x - 1, x


# 9
min_x, max_x = search_range(9, N)
log_max = max_x * log(9)
log_min = min_x * log(9)
if log_N == log_max:
    print(max_x)
    exit()
else:  # log_N < log_max
    # 6
    remaining = N - 9 ** min_x
    min_x_2, max_x_2 = search_range(6, remaining)
    log_remaining = log(remaining)
    log_max_2 = max_x_2 * log(6)
    log_min_2 = min_x_2 * log(6)
    if log_remaining == log_max_2:
        print(min_x+max_x_2)
    else:
        print(N) if min_x == 0 and min_x_2 == 0 else print(min_x+min_x_2)
