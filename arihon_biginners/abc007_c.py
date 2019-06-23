# AC
from collections import deque

# Inputs
R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
area = [list(input()) for _ in range(R)]

# Settings
already_passed = [[False] * C for _ in range(R)]
q = deque()
q.append([(sy, sx)])
n_search = 0


def BFS():
    global q
    global n_search
    global gy, gx

    curr_targets = q.popleft()
    if len(curr_targets) == 0:
        return

    confirmed = []
    for target in curr_targets:
        # Check if the target is goal
        if target[0] == gy and target[1] == gx:
            print(n_search)
            exit()

        # Check if the target is "already_passed"
        if already_passed[target[0] - 1][target[1] - 1] is True:
            continue

        """
        # Check if the target is out of range
        eval1 = target[0] < 1 or target[0] > R
        eval2 = target[1] < 1 or target[1] > C
        if eval1 or eval2:
            continue
        """

        # Check if the next points are on the load
        np1 = (target[0] + 1, target[1])
        np2 = (target[0] - 1, target[1])
        np3 = (target[0], target[1] + 1)
        np4 = (target[0], target[1] - 1)

        for np_i in [np1, np2, np3, np4]:
            if area[np_i[0] - 1][np_i[1] - 1] == '.':
                confirmed.append(np_i)

        # Mark the target as "already_passed"
        already_passed[target[0] - 1][target[1] - 1] = True

    q.append(confirmed)
    n_search += 1


# BFS
while q:
    BFS()
