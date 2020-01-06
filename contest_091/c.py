# WIP
import sys
sys_input = sys.stdin.readline

N = int(sys_input())
red_points = [tuple(map(int, sys_input().split())) for p in range(N)]
red_points = sorted(red_points, key=lambda x: (x[0]**2 + x[1]**2)**0.5)
blue_points = [tuple(map(int, sys_input().split())) for p in range(N)]
blue_points = sorted(blue_points, key=lambda x: (x[0]**2 + x[1]**2)**0.5)

red_selected = [False] * N
blue_selected = [False] * N

n_pair = 0
for blue_point in blue_points:
    for i, red_point in enumerate(red_points):
        if red_selected[i]:
            continue
        if red_point[0] < blue_point[0] and red_point[1] < blue_point[1]:
            n_pair += 1
            red_selected[i] = True
            blue_selected[i] = True
            break

print(n_pair)
