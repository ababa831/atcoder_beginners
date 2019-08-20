# AC (test cases assigned before contest)
# WA (after_contest_x)
import sys

input = sys.stdin.readline

N, Q = map(int, input().split())

link = [None] * N
for _ in range(N - 1):
    a, b = map(int, input().split())
    if link[a - 1] is None:
        link[a - 1] = [b]
    else:
        link[a - 1].append(b)

states = [0] * N

for _ in range(Q):
    p, x = map(int, input().split())
    states[p - 1] += x

for i, state in enumerate(states):
    if state == 0:
        continue
    next_nodes = link[i]
    if next_nodes is None:
        continue
    for node in next_nodes:
        states[node - 1] += state

# Output
print(*states)
