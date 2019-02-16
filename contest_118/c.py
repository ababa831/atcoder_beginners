# Accepted
from fractions import gcd 

n = int(input())
a_set = set(map(int, input().split()))
max_a = max(a_set)
min_sub = max_a

for val in a_set:
    min_sub = min(gcd(max_a, val), min_sub)
    if min_sub == 1:
        print(1)
        exit()
print(min_sub)