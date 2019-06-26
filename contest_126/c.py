# AC
# Don't use log_x function. This cause larger error.
N, K = map(int, input().split())

sum_prob = 0
for init_num in range(1, N + 1):
    if init_num < K:
        n_trial_lower = 0
        while init_num * (2**n_trial_lower) < K:
            n_trial_lower += 1
        prob = 1 / N * (0.5**n_trial_lower)
    else:
        prob = 1 / N
    sum_prob += prob

print(sum_prob)

"""
# A wrong answer:
from math import log2
 
N, K = map(int, input().split())
 
sum_prob = 0
for init_num in range(1, N + 1):
    if init_num < K:
        n_trial_lower = int(log2(K / init_num) + 1.0)
        prob = 1 / N * (0.5**n_trial_lower)
    else:
        prob = 1 / N
    sum_prob += prob
 
print(sum_prob)
"""