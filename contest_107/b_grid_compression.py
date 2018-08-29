# Use numpy if you use column operation
import numpy as np
h, w =  map(int, input().split())

# Get grid colors
gird_colors = np.array([])
for _ in range(h):
    tmp_row = np.array(list(input()))
    if "#" in tmp_row: # If the row includes black
        gird_colors = np.concatenate((gird_colors, tmp_row))
gird_colors = gird_colors.reshape(-1, w)

# Search and delete white line
del_count = 0
for wi in range(w):
    if "#" not in gird_colors[:, wi - del_count]:
        gird_colors = np.delete(gird_colors, wi - del_count, 1)
        del_count += 1

# Print result
for line_val in gird_colors:
    print("".join(line_val)) 