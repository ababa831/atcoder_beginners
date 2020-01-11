# WIP
import sys
sys_input = sys.stdin.readline

N = int(sys_input())
red_points = [tuple(map(int, sys_input().split())) for p in range(N)]
red_points = sorted(red_points, key=lambda x: (x[0]**2 + x[1]**2)**0.5)
blue_points = [tuple(map(int, sys_input().split())) for p in range(N)]
blue_points = sorted(blue_points, key=lambda x: (x[0]**2 + x[1]**2)**0.5)

# Enumerate all combinations (with duplications)
# -> How to select non-duplicated pairs?
canditates = [[None] for _ in range(N)]
for red in red_points:
    for i, blue in enumerate(blue_points):
        if red[0] < blue[0] and red[1] < blue[1]:
            canditates[i].append(red)
# WIP
