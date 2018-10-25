# Accepted, O(n)
n = int(input())
r_list = list(map(int, [input() for _ in range(n)]))

min_val = r_list[0]
max_diff = -2 * 10**9
for i in range(1, n):
    max_diff = max(max_diff, r_list[i] - min_val)
    min_val = min(min_val, r_list[i])

print(max_diff)