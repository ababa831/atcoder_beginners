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

for Cx, Cy in product(range(101), range(101)):
    last_H = None
    valid_flag = True
    counter = 0
    h_max = 0
    for i, (xi, yi, hi) in enumerate(xyh_list):
        if hi == 0:
            continue
        currnt_H = hi + abs(xi - Cx) + abs(yi - Cy)
        counter += 1
        if last_H is None:
            last_H = currnt_H
        elif last_H != currnt_H:
            valid_flag = False
            break

    if valid_flag:
        if counter != 1:
            print(Cx, Cy, last_H)
        else:
            for xi, yi, hi in xyh_list:
                if hi == 0:
                    continue
                print(xi, yi, hi)
        exit()
