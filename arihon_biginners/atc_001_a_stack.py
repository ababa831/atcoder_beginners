# Accepted
from collections import deque

H, W = map(int, input().split())

c_list = []
start_point = [None, None]  # x, y (w, h)
for idx in range(H):
    row = list(input())
    c_list.append(row)
    if 's' in row:
        start_point[0] = row.index('s')
        start_point[1] = idx


# functions
def is_road(x, y):
    out_of_width = x < 0 or x > W - 1
    out_of_hight = y < 0 or y > H - 1
    if out_of_hight or out_of_width:
        return False
    elif c_list[y][x] == '#':
        return False
    else:
        return True


def is_goal(x, y):
    if is_road(x, y):
        if c_list[y][x] == 'g':
            return True
        else:
            return False


# DFS
stack = deque()
stack.append(start_point)
while stack:
    x, y = stack.pop()
    if is_goal(x, y):
        print('Yes')
        exit()
    elif is_road(x, y):
        stack.append([x + 1, y])
        stack.append([x - 1, y])
        stack.append([x, y + 1])
        stack.append([x, y - 1])
        c_list[y][x] = '#'  # This means 'already passed'

# If you could not reach the goal
print('No')