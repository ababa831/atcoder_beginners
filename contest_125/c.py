# WA
from fractions import gcd
from itertools import combinations_with_replacement
from functools import reduce
import random


N = int(input())
a_set = set(map(int, input().split()))

origina_gcd = reduce(gcd, a_set)

n_1_combis = combinations(a_set, N)

max_gcd = origina_gcd
for combi in n_1_combis:
    tmp_gcd = reduce(gcd, combi)
    max_gcd = max(max_gcd, tmp_gcd)
print(max_gcd)