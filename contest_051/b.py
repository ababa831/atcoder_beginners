# AC
K, S = map(int, input().split())

n_combinations = 0
for x in range(K+1):
    for y in range(K+1):
        z = S - x - y
        if 0 <= z <= K:
            n_combinations += 1

print(n_combinations)

