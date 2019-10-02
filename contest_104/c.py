# WIP (WA)
import sys

sys_input = sys.stdin.readline

D, G = map(int, sys_input().split())
pc_list = [tuple(map(int, sys_input().split())) for _ in range(D)]

n_solved = 10000000000
for i in range(1 << D):
    score_per_combi = 0
    combi = []
    tmp_n_solved = 0

    for j in range(D):
        if (i >> j) & 1:
            p = pc_list[j][0]
            c = pc_list[j][1]
            score_per_combi += (j + 1) * 100 * p + c
            combi.append(j)
            tmp_n_solved += p

    if tmp_n_solved == 0:
        continue
    if score_per_combi < G:
        continue

    # problems are already sorted
    # -> check if these were oversolved
    for problem_idx in combi:
        for solved_num in range(pc_list[problem_idx][0]):
            diff = None
            if solved_num == 1:
                c = pc_list[problem_idx][1]
                diff = (problem_idx + 1) * 100 + c
                score_per_combi -= diff
            else:
                diff = (problem_idx + 1) * 100
                score_per_combi -= diff
            tmp_n_solved -= 1

            if score_per_combi < G:
                tmp_n_solved += 1
                score_per_combi += diff
                break
            # Not finish innner loop -> continue outer loop
            else:
                continue
            # Finish innner loop -> break outer loop
            break

    # Check if mininum n_solved are updated
    if tmp_n_solved < n_solved:
        n_solved = tmp_n_solved

print(n_solved)
