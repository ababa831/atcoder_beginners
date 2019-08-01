# WIP
from collections import deque

N = int(input())
hhh = list(map(int, input().split()))

n_showered = 0
max_hhh = max(hhh)

queue = deque()


def enqueue_wo_zero_elems(target_list):
    global queue, n_showered
    zero_exists = True
    cursor = -1
    while zero_exists:
        # print(zero_exists, cursor, queue)
        try:
            if cursor < len(target_list) - 1:
                zero_idx_leftmost = target_list[cursor + 1:].index(0)
                part_list = target_list[:zero_idx_leftmost]
                # print(part_list)
                if len(part_list) != 0:
                    part_list = list(map(lambda x: x - 1, part_list))
                    n_showered += 1
                    queue.append(part_list)
                cursor = zero_idx_leftmost
            else:
                zero_exists = False
        except ValueError:
            leftover = target_list[cursor + 1:]
            if len(leftover) != 0:
                queue.append(leftover)
            zero_exists = False


# Initial queing
enqueue_wo_zero_elems(hhh)

while queue:
    target_list = queue.popleft()
    enqueue_wo_zero_elems(target_list)

print(n_showered)
