N, K = map(int, input().split())

sum_p = 0
for i in range(1, N + 1):
    if i >= K:
        sum_p += 1 / N
    else:
        n_powers = 1
        while True:
            if i * (2**n_powers) >= K:
                break
            n_powers += 1
        sum_p += 1 / N * 0.5**n_powers

print(sum_p)