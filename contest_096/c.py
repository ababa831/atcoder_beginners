# WIP (DFS?, example 3 ?)
import sys
from collections import deque

sys_input = sys.stdin.readline

H, W = map(int, sys_input().split())

detected = False
start_point = None
areamap = []
for h in enumerate(range(H)):
    row = list(sys_input().replace('\n', ''))
    if not detected:
        w = row.index('#')
        start_point = [h, w]
        detected = True
    areamap.append(row)

stack = deque()
stack.append(start_point)

painted = [False for _ in range(W)] * H


def dfs():
    h_curr, w_curr = stack.pop()
    if 0 > h_curr <= H and 0 <= w_curr <= W:
        return

    mark_curr = areamap[h_curr][w_curr]
    state_curr = painted[h_curr][w_curr]
    if not state_curr and mark_curr == '#':
        painted[h_curr][w_curr] = True
        """NOTE: Wrong pattern
        stack.append(h_curr + 1, w_curr)
        stack.append(h_curr - 1, w_curr)
        stack.append(h_curr, w_curr + 1)
        stack.append(h_curr, w_curr - 1)
        """
