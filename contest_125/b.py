# AC
from itertools import combinations

N = int(input())
v_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

max_diff = -10000000
for n_selection in range(0, N+1):
    v_selected = list(combinations(v_list, n_selection))
    c_selected = list(combinations(c_list, n_selection))
    if n_selection == 0:
        max_diff = max(max_diff, 0)
    for i in range(len(v_selected)):
        X = sum(v_selected[i])
        Y = sum(c_selected[i])
        max_diff = max(max_diff, X - Y)

print(max_diff)

"""
N = int(input())
v_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

max_diff = -10000000
for selection in range(1 << N):
    v_tmp = 0
    c_tmp = 0
    for idx in range(N):
        if (selection >> idx) & 1:
            v_tmp += v_list[idx]
            c_tmp += c_list[idx]
    max_diff = max(max_diff, v_tmp - c_tmp)

print(max_diff)

"""