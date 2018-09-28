# Accepted
a, b, c, x = map(int, [input() for _ in range(4)])

n_combinations = 0
for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            if 500 * i + 100 * j + 50 * k == x:
                n_combinations += 1

print(n_combinations)