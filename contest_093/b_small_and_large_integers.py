# TLE when 01.txt was input
# You should reduce list or set operations as possible as you can
a, b, k = map(int, input().split())

int_list = [i for i in range(a, b + 1)]
out_list = sorted(set(int_list[:k] + int_list[-k:]))

for out_val in out_list:
    print(out_val)

# Updated code (Accepted)
"""
a, b, k = map(int, input().split())

lower_list = [i for i in range(a, a + k)]
upper_list = [i for i in range(b, b - k, -1)]
out_list = sorted(set(lower_list + upper_list))

for out_val in out_list:
    if a <= out_val <= b:
        print(out_val)
"""

# TODO: Examine which codes is faster.
# 1. Using list comprehension
# (I want to know if the sum of the two lists
# as shown in below takes computation time.)
"""
lower_list = [i for i in range(a, a + k)]
upper_list = [i for i in range(b, b - k, -1)]
out_list = sorted(set(lower_list + upper_list))
"""
# 2. append values to empty list
"""
out_list = []
for i in range(k):
    out_list.append(a + i)
    out_list.append(b - (k - 1 - i))
out_list = sorted(set(out_list))
"""
