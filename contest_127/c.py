N, M = map(int, input().split())

max_Li = -1
min_Ri = 10000000
for i in range(M):
    L_i, R_i = map(int, input().split())
    max_Li = max(max_Li, L_i)
    min_Ri = min(min_Ri, R_i)


print(max(0, min_Ri - max_Li + 1))
