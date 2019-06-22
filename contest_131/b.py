# AC
N, L = map(int, input().split())

abs_tastes = []
tastes = []
for i in range(1, N + 1):
    taste = L + i - 1
    abs_tastes.append(abs(taste))
    tastes.append(taste)
min_taste = min(abs_tastes)
argmin = abs_tastes.index(min_taste)
sum_taste = sum(tastes)
print(sum_taste - tastes[argmin])
