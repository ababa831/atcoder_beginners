# Accepted
n = int(input())
a = list(map(int, input().split()))

argmin_diff = None
min_diff = 100
mean_a = sum(a) / len(a)
for i, val in enumerate(a):
    diff = abs(val - mean_a)
    if diff < min_diff:
        min_diff = diff
        argmin_diff = i
print(argmin_diff)