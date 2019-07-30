# WIP
from collections import deque

N = int(input())
hhh = list(map(int, input().split()))

n_showered = 0
max_hhh = max(hhh)

queue = deque()
queue.append(hhh)

while queue:
    zero_exists = True
    cursor = -1
    target_list = queue.popleft()
    target_list = list(map(lambda x: x-1, target_list))
    n_showered += 1

    while zero_exists:
        if cursor >= N-1:
            break
        try:
            cursor = target_list.index(0)
            if len(target_list[:cursor]) != 0:
                queue.append(target_list[:cursor])
            target_list = target_list[cursor+1:]
        except ValueError:
            zero_exists = False

print(n_showered)
