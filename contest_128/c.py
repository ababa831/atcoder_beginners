N, M = map(int, input().split())

ks_lists = [list(map(int, input().split())) for _ in range(M)]
p_list = list(map(int, input().split()))


n_combi = 0
for combi in range(1 << N):
    Flag = True
    for i in range(M):
        k = ks_lists[i][0]
        s_list = ks_lists[i][1:]
        p = p_list[i]

        tmp_sum = 0
        for s in s_list:
            tmp_sum += (combi >> (s-1)) & 1
        if tmp_sum % 2 != p:
            Flag = False
            break
    if Flag:
        n_combi += 1

print(n_combi)
