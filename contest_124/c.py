S = list(input())

n_operation = 0
for i, s_val in enumerate(S):
    if i == 0:
        continue
    last_val = S[i-1]
    if s_val == last_val:
        if s_val == '0':
            S[i] = '1'
        else:
            S[i] = '0'
        n_operation += 1

print(n_operation)
    