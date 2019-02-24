# The fucking code
from itertools import combinations


n, a, b, c = map(int, input().split())
l_list = [int(input()) for _ in range(n)]
MP = 0

def update_min_and_argmin(target, l, l_list, tmp_min_diff):
    diff = target - l
    if abs(tmp_min_diff) > abs(diff):
        tmp_min_diff = diff
    return tmp_min_diff, l

def do_concat(target, l_list): 
    canditates = list(combinations(l_list, 2))
    concatted = [sum(cand) for cand in canditates]
    conc_min_diff = 10000
    for cand_concat in concatted:
        conc_min_diff, conc_at_min = update_min_and_argmin(target, cand_concat, concatted, conc_min_diff)
    arg_conc = concatted.index(conc_at_min)
    l_combi = canditates[arg_conc]
    # Do concat
    l_list.remove(l_combi[0])
    l_list.remove(l_combi[1])
    l_list.append(conc_at_min)
    return l_list


while a+b+c != 0:
    if a in l_list:
        l_list.remove(a)
        a = 0
    if b in l_list:
        l_list.remove(b)
        b = 0
    if c in l_list:
        l_list.remove(c)
        c = 0
    
    tmp_min_diff_a = 10000
    tmp_min_diff_b = 10000
    tmp_min_diff_c = 10000
    l_at_min_a = None
    l_at_min_b = None
    l_at_min_c = None
    for l in l_list:
        if a != 0:
            tmp_min_diff_a, l_at_min_a = update_min_and_argmin(a, l, l_list, tmp_min_diff_a)
        if b != 0:
            tmp_min_diff_b, l_at_min_b = update_min_and_argmin(b, l, l_list, tmp_min_diff_b)
        if c != 0:
            tmp_min_diff_c, l_at_min_c = update_min_and_argmin(c, l, l_list, tmp_min_diff_c)
    
    if abs(tmp_min_diff_a) < 10:
        MP += tmp_min_diff_a
        a = 0
        l_list.remove(l_at_min_a)
    if abs(tmp_min_diff_b) < 10:
        MP += tmp_min_diff_b
        b = 0
        l_list.remove(l_at_min_b)
    if abs(tmp_min_diff_c) < 10:
        MP += tmp_min_diff_c
        c = 0
        l_list.remove(l_at_min_c)
    
    for idx, target in enumerate([a, b, c]):
        if target != 0:
            l_list = do_concat(target, l_list)
            MP += 10

print(MP)