# TLE
from collections import deque


N, Q = map(int, input().split())

link = [None] * N
for _ in range(N-1):
    a, b = map(int, input().split())
    if link[a-1] is None:
        link[a-1] = [b]
    else:
        link[a-1].append(b)

states = [0] * N
stack = deque()


def dfs(x):
    p = stack.popleft()

    # Add score
    states[p-1] += x
    # Search nexts
    nexts = link[p-1]
    if nexts is None:
        return
    for next_node in nexts:
        stack.append(next_node)


def update(p, x):
    stack.append(p)
    while stack:
        dfs(x)


for _ in range(Q):
    p, x = map(int, input().split())
    update(p, x)

# Output
print(' '.join(map(str, states)))
