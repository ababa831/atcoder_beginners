# AC
from itertools import combinations

N = int(input())
SSS = [input() for _ in range(N)]

# Filter1
filter_1 = {'M', 'A', 'R', 'C', 'H'}
canditates = [S for S in SSS if S[0] in filter_1]
cand_inits = [c[0] for c in canditates]
cand_inits_set = set(cand_inits)
init_counts = {init_c: cand_inits.count(init_c) for init_c in filter_1}

n_combi = 0
for init_combi in combinations(cand_inits_set, 3):
    tmp_combi = 1
    for init_c in init_combi:
        tmp_combi *= init_counts[init_c]

    n_combi += tmp_combi

print(n_combi)
