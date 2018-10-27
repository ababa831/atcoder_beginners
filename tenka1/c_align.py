# Due to the input size:2<p<=10^5, O(n) -> TLE
from itertools import permutations
import math

n = int(input())
a_list = sort(list(map(int, [input() for _ in range(n)])))

#####
len_alist = len(a_list)

p = permutations(a_list, len_alist)
max_p_diff = 0
for p_val in p:
    tmp_diff_sum = sum([abs(p_val[i+1] - p_val[i]) for i in range(len_alist - 1)])
    max_p_diff = max(max_p_diff, tmp_diff_sum)

print(max_p_diff)

#### Draft of a modified code (In progress)
"""
median = int(len_alist/2)
max_p_diff = 0
if len_alist % 2:
    last_elem = a_list[median]
    smaller_list = a_list[:median]
    larger_list = a_list[median+1:]
    p_smaller = permutations(smaller_list, median)
    p_larger = permutations(larger_list, median)

    for pval_s in p_smaller:
        for pval_l in p_larger:
            canditate_1 = []
            canditate_2 = []
            for i in range(median):
                canditate_1.append(pval_s[i])
                canditate_1.append(pval_l[i])
                canditate_2.append(pval_l[i])
                canditate_2.append(pval_s[i])
            canditate_1 += [last_elem]
            canditate_2 += [last_elem]

            # Calc sum of diffs
            tmp_diffs_sum = 
"""