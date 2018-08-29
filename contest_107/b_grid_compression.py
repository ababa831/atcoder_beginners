# Use numpy if you use column operation
import numpy as np
h, w =  map(int, input().split())

# Get grid colors
grid_colors = np.array([])
for _ in range(h):
    tmp_row = np.array(list(input()))
    if "#" in tmp_row: # If the row includes black
        grid_colors = np.concatenate((grid_colors, tmp_row))
grid_colors = grid_colors.reshape(-1, w)

# Search and delete white line
del_count = 0
for wi in range(w):
    if "#" not in grid_colors[:, wi - del_count]:
        grid_colors = np.delete(grid_colors, wi - del_count, 1)
        del_count += 1

# Print result
for line_val in grid_colors:
    print("".join(line_val))

"""
Tip:
When you search columns in 2D-list, use zip(*2D_list) as shown in below example code.

h, w = map(int, input().split())
grid_colors = [input() for _ in range(h)]
grid_colors = list(filter(lambda row: any(x == '#' for x in row), grid_colors))
grid_colors = list(filter(lambda col: any(x == '#' for x in col), zip(*grid_colors)))
for row in zip(*grid_colors):
    print(''.join(row))
"""