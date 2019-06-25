N, M = map(int, input().split())

max_L = -1
min_R = 10**5 + 1
for _ in range(M):
    L, R = map(int, input().split())
    max_L = max(max_L, L)
    min_R = min(min_R, R)

print(max(min_R - max_L + 1, 0))
