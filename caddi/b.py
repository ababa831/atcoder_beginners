# Accepted
n, h, w = map(int, input().split())
n_splittable = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a>= h and b >= w:
        n_splittable += 1

print(n_splittable)
