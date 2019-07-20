# AC
from collections import deque

N, A, B, C = map(int, input().split())
lll = [int(input()) for _ in range(N)]

stack = deque()
init_data = (0, [])
stack.append(init_data)

mp_results = []


def dfs():
    depth, curr_path = stack.pop()
    if depth == N:
        filter_a = 'A' not in curr_path
        filter_b = 'B' not in curr_path
        filter_c = 'C' not in curr_path
        if filter_a or filter_b or filter_c:
            return
        a_combi, b_combi, c_combi = [], [], []
        for idx, history in enumerate(curr_path):
            if history == 'A':
                a_combi.append(lll[idx])
            elif history == 'B':
                b_combi.append(lll[idx])
            elif history == 'C':
                c_combi.append(lll[idx])
        n_concat = len(a_combi)-1 + len(b_combi)-1 + len(c_combi)-1
        mp_used_for_concat = n_concat * 10
        mp_used_for_ext_shr = \
            abs(A-sum(a_combi)) + abs(B-sum(b_combi)) + abs(C-sum(c_combi))

        mp_results.append(mp_used_for_concat + mp_used_for_ext_shr)
    else:
        depth += 1
        stack.append((depth, curr_path + ['A']))
        stack.append((depth, curr_path + ['B']))
        stack.append((depth, curr_path + ['C']))
        stack.append((depth, curr_path + ['O']))


while stack:
    dfs()

print(min(mp_results))
