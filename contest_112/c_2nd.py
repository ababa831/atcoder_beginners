# AC
"""memo:
for Cx, Cy in zip(range(0, 101), range(0, 101))
hi + abs(Xi-Cx)+abs(Yi-Cy) == hj + abs(Xj-Cx)+abs(Yj-Cy)
in All points

Complexity: 101 * 101 * N -> Max: 101 * 101 * 100 = 1020100
"""
import sys
from itertools import product

input = sys.stdin.readline

N = int(input())
xyh_list = [tuple(map(int, input().split())) for _ in range(N)]

# There is one point where hi == 1:
non0_hhh = []
for x, y, h in xyh_list:
    if h != 0:
        non0_hhh.append([x, y, h])
if len(non0_hhh) == 1:
    print(*non0_hhh[0])
    exit()

for Cx, Cy in product(range(101), range(101)):
    last_H = None
    valid_flag = True
    for i, (xi, yi, hi) in enumerate(xyh_list):
        if hi == 0:
            continue
        currnt_H = hi + abs(xi - Cx) + abs(yi - Cy)
        if last_H is None:
            last_H = currnt_H
        elif last_H != currnt_H:
            valid_flag = False
            break

    if valid_flag:
        print(Cx, Cy, last_H)
        exit()
