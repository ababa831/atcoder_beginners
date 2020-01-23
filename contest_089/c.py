# WIP
from itertools import combinations

N = int(input())
SSS = [input() for _ in range(N)]

# Filter1
filter_1 = {'M', 'A', 'R', 'C', 'H'}
canditates = set([S for S in SSS if S[0] in filter_1])
cand_inits = [c[0] for c in canditates]
init_counts = {init_c: cand_inits.count(init_c) for init_c in filter_1}

# TODO: Deal with duplication
# e.g. {C, M1, M2, R1, R2, A}
# patterns: {[C, M, R], [C, M, A], [C, R, A], [M, R, A]}
#    pattern = 4C3  # 4 means len([C, M, R, A])  
#    if M and R in pattern:
#       combi1 = pattern * n_Mgroup * n_Rgroup
#    if M in pattern:
#       combi2 = pattern * n_Mgroup
#    if R in pattern:
#       combi3 = pattern * n_Rgroup
# total_combinations = combi1 + combi2 + combi3 - (N-n_Mgroup-n_Rgroup)C3
