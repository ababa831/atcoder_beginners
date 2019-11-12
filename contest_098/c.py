# AC (Cumulative sum?)
N = int(input())
S = input()

num_E, num_W = 0, 0
# num_E_list = [0] * (N + 1)
# num_W_list = [0] * (N + 1)
min_sum_operation = N
argmin_i = 0
for i, c in enumerate(S):
    if i == 0:
        # This operation is safe because N is larger than 2
        right = S[i + 1:]
        num_E = right.count('E')
        num_W += 1 if c == 'W' else 0
        # num_E_list[i] = num_E
        # num_W_list[i] = num_W
    elif c == 'W':
        num_W += 1
        # num_W_list[i + 1] = num_W
    elif c == 'E':
        num_E -= 1
        # num_E_list[i] = num_E
    if min_sum_operation > num_E + num_W:
        min_sum_operation = min(min_sum_operation, num_E + num_W)
        argmin_i = i

    # print(min_sum_operation, num_E, num_W)

if argmin_i == 0:
    print(min_sum_operation - 1)
else:
    print(min_sum_operation)
