# WIP (WA: 1_01.txt, 1_06.txt, 1_07.txt)
import sys
input_s = sys.stdin.readline

N, K = map(int, input_s().split())
xxx = list(map(int, input_s().split()))
if K == 1:
    xxx = [abs(x) for x in xxx]
    print(min(xxx))
    exit()

# Select candles
min_distance = 10000000000
arg_min = 100000000
for i in range(N-K+1):
    tmp_larger = max(abs(xxx[i]), abs(xxx[i+K-1]))
    if tmp_larger < min_distance:
        arg_min = i
        min_distance = tmp_larger

# Select route
candles = xxx[arg_min:arg_min+K]
left_edge = candles[0]
right_edge = candles[-1]
left_edge_dist = abs(left_edge)
right_edge_dist = abs(right_edge)
if left_edge > 0:
    print(right_edge)
elif right_edge < 0:
    print(abs(left_edge))
elif left_edge_dist > right_edge_dist:
    print(right_edge_dist*2+left_edge_dist)
else:
    print(left_edge_dist*2+right_edge_dist)
