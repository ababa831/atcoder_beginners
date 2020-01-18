# WIP
from itertools import combinations

N = int(input())
SSS = [input() for _ in range(N)]

# Filter1
filter_1 = {'M', 'A', 'R', 'C', 'H'}
canditates = [S for S in SSS if S[0] in filter_1]
cand_inits = [c[0] for c in canditates]
init_counts = {init_c: cand_inits.count(init_c) for init_c in filter_1}
