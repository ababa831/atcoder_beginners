# AC (I mixed up the problem intent)
import sys


sys_input = sys.stdin.readline

H, W = map(int, sys_input().split())

areamap = []
areamap.append(['.']*(W+2))
for h in enumerate(range(H)):
    row = list(sys_input().replace('\n', ''))
    row = ['.'] + row + ['.']
    areamap.append(row)
areamap.append(['.']*(W+2))

for h in range(1, H+1):
    for w in range(1, W+1):
        if areamap[h][w] == '#' and \
                areamap[h][w+1] == '.' and \
                areamap[h][w-1] == '.' and \
                areamap[h+1][w] == '.' and \
                areamap[h-1][w] == '.':
            print('No')
            exit()

print('Yes')
