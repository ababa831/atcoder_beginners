# WA, the fucking code
N, M = map(int, input().split())
A_list_sorted = sorted(list(map(int, input().split())))

for i in range(M):
    B_i, C_i = map(int, input().split())
    n_changed = 0
    for k, A in enumerate(A_list_sorted):
        if A < C_i and n_changed < B_i:
            A_list_sorted[k] = C_i
            n_changed += 1
        elif n_changed >= B_i:
            break

print(sum(A_list_sorted))
