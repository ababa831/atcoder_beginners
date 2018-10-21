# Accepted
h, w = map(int, input().split())
# Setting
mine_set = set()
next_to_grid_list = [(1, 0), (1, -1), (0, -1), (-1, -1), 
                     (-1, 0), (-1, 1), (0, 1), (1, 1)]


def add_number_for_dot(mine):
    for next_to_grid in next_to_grid_list:
        if is_constrained(mine[0] + next_to_grid[0], mine[1] + next_to_grid[1]):
            if type(grids[mine[0] + next_to_grid[0]][mine[1] + next_to_grid[1]]) is int:
                grids[mine[0] + next_to_grid[0]][mine[1] + next_to_grid[1]] += 1


def is_constrained(i, j):
    if 0 <= i < h and 0 <= j < w:
        return True
    else:
        return False


# Register grids information
grids = []
for i in range(h):
    grids.append(list(input()))
    for j in range(w):
        if grids[i][j] == "#":
            mine_set.add((i, j))
        else:
            grids[i][j] = 0

# add number to "."
for mine in mine_set:
    add_number_for_dot(mine)

# Show result
for i in range(h):
    s_i = [str(grid) if type(grid) is int else grid for grid in grids[i]]
    print("".join(s_i))