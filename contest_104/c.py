import sys
from itertools import combinations

sys_input = sys.stdin.readline

D, G = map(int, input().split())
pc_list = [tuple(map(int, input().split())) for _ in range(D)]

# WIP
temp_min_score = 0
for i in range(1 << len(D)):
    score_per_combi = 0
    combi = []
    combi_min = []
    for j in range(len(D)):
        if (i >> j) & 1:
            p = pc_list[j][0]
            c = pc_list[j][1]
            score_per_combi += (j + 1) * 100 * p + c
            combi.append(j)
    if score_per_combi >= G:
        temp_min_score = min(temp_min_score, score_per_combi)
        combi_min = combi
