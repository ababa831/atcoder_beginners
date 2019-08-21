import sys
from collections import deque

stack = deque()
input = sys.stdin.readline

N, Q = map(int, input().split())

link = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    link[a - 1].append(b)
    link[b - 1].append(a)

states = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    states[p - 1] += x

check = [0] * N
stack.append(1)
check[0] = 1
while stack:
    node = stack.pop()
    for next_node in link[node - 1]:
        if check[next_node - 1]:
            continue
        states[next_node - 1] += states[node - 1]
        check[next_node - 1] = 1
        stack.append(next_node)

# Output
print(*states)
