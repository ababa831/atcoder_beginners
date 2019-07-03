# AC
N, M = map(int, input().split())
AB_list = [list(map(int, input().split())) for _ in range(N)]
AB_list = sorted(AB_list, key=lambda x: x[0])

sum_cost = 0
n_drink = 0
for AB in AB_list:
    A, B = AB
    if n_drink + B < M:
        n_drink += B
        sum_cost += A * B
    elif n_drink + B >= M:
        sum_cost += A * (M - n_drink)
        print(sum_cost)
        exit()
