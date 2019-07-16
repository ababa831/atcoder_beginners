# WIP
from collections import deque
from copy import deepcopy


N, A, B, C = map(int, input().split())
lll = [int(input()) for _ in range(N)]

# Settings
stack = deque()
reached_mps = []

bamboo_states = [lll, 0]  # [lll, MP==0]
stack.append(bamboo_states)


def dfs():
    curr_bamboos = stack.pop()
    curr_lll = curr_bamboos[0]
    mp = curr_bamboos[1]

    # If reached goal
    if 'A' in curr_lll and 'B' in curr_lll and 'C' in curr_lll:
        reached_mps.append(mp)
        return

    for idx, l_val in enumerate(curr_lll):
        # If reached A or B or C
        if 'A' not in curr_lll and l_val == A:
            curr_bamboos[0][idx] = 'A'
            stack.append(curr_bamboos)
            continue
        elif 'B' not in curr_lll and l_val == B:
            curr_bamboos[0][idx] = 'B'
            stack.append(curr_bamboos)
            continue
        elif 'C' not in curr_lll and l_val == C:
            curr_bamboos[0][idx] = 'C'
            stack.append(curr_bamboos)
            continue

        if isinstance(l_val, str):
            continue
        if l_val is None:
            continue
        if l_val <= 0:
            curr_bamboos[idx] = None
            continue
        # Add new bamboo states to the stack
        # The fucking code.
        # - extend
        extended_bamboos = deepcopy(curr_bamboos)
        extended_bamboos[0][idx] = l_val + 1
        extended_bamboos[1] = mp + 1
        stack.append(extended_bamboos)
        # - shrink
        shrinked_bamboos = deepcopy(curr_bamboos)
        shrinked_bamboos[0][idx] = l_val - 1
        shrinked_bamboos[1] = mp + 1
        stack.append(shrinked_bamboos)
        # - concatnate with another bamboo
        for another_idx, another_len in enumerate(curr_lll):
            if idx == another_idx or isinstance(another_len, str):
                continue
            concatted_bamboos = deepcopy(curr_bamboos)
            concatted_bamboos[0][another_idx] = another_len + l_val
            concatted_bamboos[1] = mp + 10
            concatted_bamboos[0][idx] = None
            stack.append(concatted_bamboos)


while stack:
    dfs()

print(min(reached_mps))
