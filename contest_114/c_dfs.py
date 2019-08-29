# An example answer by DFS
# AC
from collections import deque

N = int(input())

stack = deque()
num_753 = 0


def dfs():
    global stack, num_753

    s = stack.pop()

    if int(s) > N:
        return

    is_contained = 1 if all(s.count(c) > 0 for c in '753') else 0
    num_753 += is_contained

    for next_s in '357':
        stack.append(s + next_s)


stack.append('0')
while stack:
    dfs()

# Output
print(num_753)
