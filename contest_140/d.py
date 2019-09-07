# WA
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = input()

last = ''
sep_idcs = [0]
base_happiness = 0
for i, c in enumerate(S):
    if i != 0:
        if last != c:
            base_happiness += i - sep_idcs[-1] - 1
            sep_idcs.append(i)
    last = c
# The right edge
len_seps = len(sep_idcs)
if len_seps == 3:
    base_happiness -= 1

# print(sep_idcs)
if len_seps % 2 and K == len_seps / 2:
    print(base_happiness + 2 * K - 1)
else:
    print(base_happiness + 2 * K)
