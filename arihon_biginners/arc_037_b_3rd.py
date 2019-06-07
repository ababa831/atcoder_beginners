# WA
# Not implement DFS
from copy import copy

N, M = map(int, input().split())

srcs = []
dsts = []
for _ in range(M):
    src, dst = map(int, input().split())
    srcs.append(src)
    dsts.append(dst)

n_tree = 0
check_point = 0
for m_i in range(M):
    dst_curr = dsts[m_i]
    if m_i < M-1:
        next_src = srcs[m_i+1]
        continuity_evaluator = next_src - dst_curr
        if continuity_evaluator > 0:
            penalty = 0
            if len(set(dsts[check_point:m_i+1])) != len(dsts[check_point:m_i+1]):
                penalty = 1
            n_tree += continuity_evaluator - penalty
            check_point = copy(m_i)
    else:
        penalty = 0
        if len(set(dsts[check_point:m_i+1])) != len(dsts[check_point:m_i+1]):
            penalty = 1
        n_tree += N - dst_curr + 1 - penalty

# Output
print(n_tree)
