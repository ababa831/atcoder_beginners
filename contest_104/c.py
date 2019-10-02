# WIP (WA, a01, a04, b05, b20~b24)
import sys

sys_input = sys.stdin.readline

D, G = map(int, sys_input().split())
pc_list = [tuple(map(int, sys_input().split())) for _ in range(D)]

temp_min_score = 10000000000000000
combi_min = []
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
    if score_per_combi >= G and tmp_n_solved < n_solved:
        temp_min_score = score_per_combi
        combi_min = combi
        n_solved = tmp_n_solved

# problems are already sorted
# -> check the problems were oversolved
tmp_reduced = temp_min_score
for problem_idx in combi_min:
    for solved_num in range(pc_list[problem_idx][0]):
        if solved_num == 1:
            c = pc_list[problem_idx][1]
            diff = (problem_idx + 1) * 100 + c
            tmp_reduced -= diff
        else:
            diff = (problem_idx + 1) * 100
            tmp_reduced -= diff
        n_solved -= 1

        if tmp_reduced < G:
            print(n_solved + 1)
            exit()

print(n_solved)
