# AC
import math

n_paths = 5
N = int(input())
ABCDE = [int(input()) for _ in range(n_paths)]

bottleneck = min(ABCDE)
n_addition = math.ceil(N / bottleneck) - 1
print(n_paths + n_addition)
