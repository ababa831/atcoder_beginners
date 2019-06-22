from collections import deque
 
N, M = map(int, input().split())
 
connect = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    connect[u - 1].append(v)
    connect[v - 1].append(u)
 
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
 
    prev_node, curr_node = queue.popleft()
    already_passed[curr_node - 1] = True
 
    next_nodes = connect[curr_node - 1]
    for next_node in next_nodes:
        if next_node == prev_node:
            continue
        elif already_passed[next_node - 1]:
            is_tree = False
            return
        else:
            queue.append([curr_node, next_node])
 
 
n_tree = 0
prev = -1
for i in range(1, N + 1):
    if not already_passed[i - 1]:
        queue.append([prev, i])
        while queue:
            # print(queue)
            DFS()
            # print(queue)
            # print(is_tree)
        if is_tree:
            n_tree += 1
    # Reset settings
    is_tree = True
 
print(n_tree)
