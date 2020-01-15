# WA (Only one testcase: 'maxrand_2')
import sys
sys_input = sys.stdin.readline

N = int(sys_input())
red_points = [tuple(map(int, sys_input().split())) for p in range(N)]
red_points = sorted(red_points, key=lambda x: (x[0]**2 + x[1]**2)**0.5)
blue_points = [tuple(map(int, sys_input().split())) for p in range(N)]
blue_points = sorted(blue_points, key=lambda x: (x[0]**2 + x[1]**2)**0.5)

# Enumerate all combinations (with duplications)
# -> How to select non-duplicated pairs?
canditates = [[] for _ in range(N)]
for red in red_points:
    for i, blue in enumerate(blue_points):
        if red[0] < blue[0] and red[1] < blue[1]:
            canditates[i].append(red)


canditates = sorted(canditates, key=lambda x: len(x))
n_combi = 0
already_selected = []
for i, cand in enumerate(canditates[:N-1]):
    point_at_min_appear = None
    min_n_appear = N
    for point in cand:
        if point in already_selected:
            continue
        n_appear = 0
        for cand_ano in canditates[i+1:]:
            if point in cand_ano:
                n_appear += 1
        if min_n_appear > n_appear:
            point_at_min_appear = point
    
    if point_at_min_appear is not None:
        n_combi += 1
        already_selected.append(point_at_min_appear)

# last element
last_points = canditates[-1]
for point in last_points:
    if point not in already_selected:
        n_combi += 1
        break

print(n_combi)
