# WA, something wrong when checked a04, a16
import math

D, G = map(int, input().split())
p_c_list = [list(map(int, input().split())) for _ in range(D)]

min_num_solved = 1000000000000000000000
for canditate in range(1 << D):
    num_solved = 0
    score = 0
    digit_m1_list = []
    # digit_m1 means digit - 1
    d_range = range(D)
    for digit_m1 in d_range:
        # If all problems were solved
        if (canditate >> digit_m1) & 1:
            digit = digit_m1 + 1
            score += \
                (100 * digit) * p_c_list[digit_m1][0] + p_c_list[digit_m1][1]
            num_solved += p_c_list[digit_m1][0]
            digit_m1_list.append(digit_m1)
    # print('digit_m1: ', digit_m1_list, 'score: ', score, 'n_solved: ', num_solved)

    # If the score did not reach the (G)oal point
    if score < G:
        left_point = G - score
        left_probrems_idxes_m1 = \
            [i for i in reversed(d_range) if i not in digit_m1_list]
        # Calcurate How many probrems you should solve
        # Constraint: 100 * (left_probrems_idx_m1 + 1) * x >= left_point
        # ->  x >= left_point / (100 * (left_probrems_idx_m1 + 1))
        for left_probrems_idx_m1 in left_probrems_idxes_m1:
            x = math.ceil(left_point / (100 * (left_probrems_idx_m1 + 1)))
            # p_c_list[left_probrems_idx_m1][0] : Total probrems in the idx
            num_solved += min(p_c_list[left_probrems_idx_m1][0], x)
            left_point -= (100 * (left_probrems_idx_m1 + 1)) * num_solved
            if left_point <= 0:
                # print('if you additionally solved probrems -> n_solved: ', num_solved)
                break
    min_num_solved = min(min_num_solved, num_solved)

print(min_num_solved)
