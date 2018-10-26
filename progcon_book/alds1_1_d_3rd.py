# Accepted
n = int(input())
s_list = list(map(int, [input() for _ in range(n)]))

min_val = s_list[0]
max_diff = -2 * 10**9
for i in range(1, n):
    max_diff = max(max_diff, s_list[i] - min_val)
    min_val = min(min_val, s_list[i])

print(max_diff)