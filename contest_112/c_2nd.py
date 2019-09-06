# WIP
import sys
input = sys.stdin.readline

N = int(input())
xyh_list = [tuple(map(int, input().split())) for _ in range(N)]

"""memo:
for Cx, Cy in zip(range(0, 101), range(0, 101))
hi + abs(Xi-Cx)+abs(Yi-Cy) == hj + abs(Xj-Cx)+abs(Yj-Cy)
in All points
"""
