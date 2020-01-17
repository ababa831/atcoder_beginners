# AC
N, M = map(int, input().split())

if N == 1 and M == 1:
    print(1)
elif N == 1:
    print(M - 2 if M > 2 else 0)
elif M == 1:
    print(N - 2 if N > 2 else 0)
elif N > 2 and M > 2:
    print((N - 2) * (M - 2))
else:
    print(0)

"""
# An experiment
n_count_map = [[0 for _ in range(M)] for _ in range(N)]


def update(x, y):
    # Count
    n_count_map[y][x] += 1
    if y + 1 < N:
        n_count_map[y + 1][x] += 1
    if y - 1 >= 0:
        n_count_map[y - 1][x] += 1
    if x + 1 < M:
        n_count_map[y][x + 1] += 1
    if x - 1 >= 0:
        n_count_map[y][x - 1] += 1
    if y + 1 < N and x + 1 < M:
        n_count_map[y + 1][x + 1] += 1
    if y - 1 >= 0 and x - 1 >= 0:
        n_count_map[y - 1][x - 1] += 1
    if y + 1 < N and x - 1 >= 0:
        n_count_map[y + 1][x - 1] += 1
    if y - 1 >= 0 and x + 1 < M:
        n_count_map[y - 1][x + 1] += 1


for n in range(N):
    for m in range(M):
        update(m, n)

print(n_count_map)
"""
