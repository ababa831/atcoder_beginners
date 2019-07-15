# AC
N, M = map(int, input().split())

AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda x: x[0])

n_drink = 0
cost = 0
for A, B in AB:
    remaining = M - n_drink
    if remaining > B:
        n_drink += B
        cost += A * B
    elif remaining <= B:
        cost += A * remaining
        print(cost)
        exit()
