# AC
N, M = map(int, input().split())
A_list = sorted(list(map(int, input().split())))

BC_list = [tuple(map(int, input().split())) for _ in range(M)]
BC_list.sort(key=lambda x: x[1], reverse=True)

n_replace = 0
sum_target = 0
is_broken = False
for B, C in BC_list:
    if n_replace + B <= N:
        for A in A_list[n_replace:n_replace+B]:
            if A < C:
                sum_target += C
                n_replace += 1
            else:
                is_broken = True
                break
    else:
        remaining = N - n_replace
        for A in A_list[n_replace:n_replace+remaining]:
            if A < C:
                sum_target += C
                n_replace += 1
            else:
                is_broken = True
                break
    if is_broken is True:
        break
if n_replace < N:
    sum_target += sum(A_list[n_replace:])

# Output sumed A_list
print(sum_target)
