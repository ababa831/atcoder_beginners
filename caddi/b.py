# Accepted
n, h, w = map(int, input().split())
n_splitable = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a>= h and b >= w:
        n_splitable += 1

print(n_splitable)
