# WIP (Something wrong)
from collections import deque

N, M = map(int, input().split())
connect = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    connect[u - 1].append(v)
    connect[v - 1].append(u)

# Settings
already_passed = [False] * N
stack = deque()
n_tree = 0
is_tree = True
curr_max = -1


def DFS():
    global is_tree
    global curr_max
    global already_passed

    curr_node = stack.pop()
    next_nodes = []
    if not already_passed[curr_node - 1]:
        next_nodes = connect[curr_node - 1]
        for next_node in next_nodes:
            stack.append(next_node)
        already_passed[curr_node - 1] = True
    else:
        is_tree = False
    curr_max = max(curr_max, curr_node)


stack.append(1)
while True:
    while stack:
        print(is_tree)
        DFS()
    if is_tree:
        n_tree += 1
    jump_to = curr_max + 1
    if jump_to <= N:
        stack.append(jump_to)
    else:
        break
    is_tree = True

print(n_tree)
