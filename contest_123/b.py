# Accepted
import itertools
import math

dishes = list(map(int, [input() for _ in range(5)]))
p_list = list(itertools.permutations(dishes))

min_total_time = 1000000000
for p in p_list:
    next_time = 0
    for idx, dish in enumerate(p):
        if idx <= 3:
            next_time = math.ceil((next_time + dish) / 10) * 10
        else:
            next_time += dish
    min_total_time = min(min_total_time, next_time)

print(min_total_time)
