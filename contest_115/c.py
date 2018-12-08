# Accepted
n, k = map(int, input().split())
h_list = list(map(int, [input() for _ in range(n)]))
h_list = sorted(h_list, reverse=True)

min_diff = 10**9
for i in range(n - k + 1):
    h_max = h_list[i]
    h_min = h_list[i + k - 1]
    h_diff = h_max - h_min
    if min_diff > h_diff:
        min_diff = h_diff
    if min_diff == 0:
        print(0)
        exit()
print(min_diff)