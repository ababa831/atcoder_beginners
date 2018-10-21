# In progress
h, w = map(int, input().split())
# Setting
mine_set = set()


def add_number_for_dot(mine):
    if is_constrained(mine[0] + 1, mine[1] + 0]) and type(grids[mine[0] + 1][mine[1] + 0]) is int:
        grids[mine[0] + 1][mine[1] + 0] += 1
    if type(grids[mine[0] + 1][mine[1] - 1]) is int:
        grids[mine[0] + 1][mine[1] - 1] += 1
    if type(grids[mine[0] + 0][mine[1] - 1]) is int:
        grids[mine[0] + 0][mine[1] - 1] += 1
    if type(grids[mine[0] - 1][mine[1] - 1]) is int:
        grids[mine[0] - 1][mine[1] - 1] += 1
    if type(grids[mine[0] - 1][mine[1] + 0]) is int:
        grids[mine[0] - 1][mine[1] + 0] += 1
    if type(grids[mine[0] - 1][mine[1] + 1]) is int:
        grids[mine[0] - 1][mine[1] + 1] += 1
    if type(grids[mine[0] + 0][mine[1] + 1]) is int:
        grids[mine[0] + 0][mine[1] + 1] += 1
    if type(grids[mine[0] + 1][mine[1] + 1]) is int:
        grids[mine[0] + 1][mine[1] + 1] += 1


def is_constrained(i, j):
    if 0 <= i < h or 0 <= j < w:
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

for i in range(h):
    s_i = [str(grid) if type(grid) is int else grid for grid in grids[i]]
    print("".join(s_i))