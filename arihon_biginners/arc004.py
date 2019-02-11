# Accepted
import math

n = int(input())
coord_list = [list(map(int, input().split())) for _ in range(n)]

max_len = 0
for i, p1 in enumerate(coord_list[:n - 1]):
    for p2 in coord_list[i:n]:
        temp_len = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        if temp_len > max_len:
            max_len = temp_len

print(max_len)
