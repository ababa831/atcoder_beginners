import sys

sys_input = sys.stdin.readline

H, W = map(int, sys_input().split())
areamap = [list(sys_input().replace('\n', '')) for h in range(H)]

print(H, W)
print(areamap)
