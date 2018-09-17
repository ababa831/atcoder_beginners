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

