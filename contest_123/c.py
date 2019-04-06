import math

n = int(input())
transportations = list(map(int, [input() for _ in range(5)]))

min_trans = min(transportations)

print(4 + math.ceil(n / min_trans))
