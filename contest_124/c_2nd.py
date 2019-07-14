# AC
S = list(map(int, list(input())))

last = S[0]
n_change = 0
for idx, current in enumerate(S):
    if idx == 0:
        continue
    if current == last:
        current = 0 if current == 1 else 1
        S[idx] = current
        n_change += 1
    last = current

print(n_change)
