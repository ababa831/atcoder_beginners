# TLE (Only 1 test case!)
from math import factorial
from copy import copy

N, M = map(int, input().split())

all_patterns = 1
start, end = None, None
for m_i in range(M + 1):
    if m_i < M:
        a_i = int(input())
    if m_i == 0:
        start = 0
        end = a_i - 1
        next_start = a_i + 1
    elif m_i == M:
        start = copy(next_start)
        end = N
    else:
        start = copy(next_start)
        end = a_i - 1
        next_start = a_i + 1
    passdiff = end - start
    num_2 = passdiff // 2
    residue = passdiff % 2

    tmp_patterns_for_range = 0
    for num2to1 in range(num_2 + 1):
        add_n_1 = num2to1 * 2
        tmp_num2 = num_2 - num2to1
        tmp_n_pattern = \
            factorial(tmp_num2 + add_n_1 + residue) \
            // factorial(tmp_num2) \
            // factorial(add_n_1 + residue)
        tmp_patterns_for_range += tmp_n_pattern
    all_patterns *= tmp_patterns_for_range

print(all_patterns % 1000000007)
