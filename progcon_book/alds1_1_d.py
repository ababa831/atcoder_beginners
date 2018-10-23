# TLE, O(n^2)
n = int(input())
r_list = list(map(int, [input() for _ in range(n)]))

max_diff = -10**(9) -1
for i in range(n):
    for j in range(i+1, n):
            tmp_diff = r_list[j] - r_list[i]
            if tmp_diff > max_diff:
                max_diff = tmp_diff

print(max_diff)