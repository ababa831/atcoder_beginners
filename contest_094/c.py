# Median calculation is executed fist time only
# WA
import sys

sys_input = sys.stdin.readline

N = input()
XXX = list(map(int, sys_input().split()))

XXX_sorted = sorted(XXX)
init_median = XXX_sorted[1:][len(XXX) // 2 - 1]
print(init_median)

last_median = init_median
last_X = XXX[0]
last_cursor = len(XXX) // 2 - 1 if last_median < XXX[0] else len(XXX) // 2
for X in XXX[1:]:
    flg1 = last_X > last_median >= X
    flg2 = last_X < last_median <= X
    if flg1:
        last_cursor += 1
        last_median = XXX_sorted[last_cursor]
    if flg2:
        last_cursor -= 1
        last_median = XXX_sorted[last_cursor]
    print(last_median)
    last_X = X
