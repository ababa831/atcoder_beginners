# Accepted
n = int(input())

total = 0
for _ in range(n):
    x, u = input().split()
    x = float(x)
    if u == 'BTC':
        x = 380000.0 * x
    total += x
print(total)