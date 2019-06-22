# WA
from collections import deque

N, M = map(int, input().split())

connect = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    connect[u - 1].append(v)
    # connect[v - 1].append(u)

# print(connect)

# Global settings
already_passed = [False] * N
queue = deque()
is_tree = True
max_in_graph = 1


def DFS():
    # Global variables
    global already_passed
    global queue
    global is_tree
    global max_in_graph
    
    curr_node = queue.popleft()

    if already_passed[curr_node - 1]:
        is_tree = False
    else:
        nexts = connect[curr_node - 1]

        curr_max = -1
        if len(nexts) != 0:
            curr_max = max(nexts)
            for n in nexts:
                queue.append(n)
        else:
            curr_max = curr_node

        already_passed[curr_node - 1] = True
        max_in_graph = max(curr_max, max_in_graph)


n_tree = 0
jump_to = 1
while jump_to <= N:
    queue.append(jump_to)
    while queue:
        # print(queue)
        DFS()
        # print(queue)
        # print(is_tree)
    if is_tree:
        n_tree += 1
    # Reset settings
    is_tree = True
    jump_to = max_in_graph + 1

print(n_tree)
