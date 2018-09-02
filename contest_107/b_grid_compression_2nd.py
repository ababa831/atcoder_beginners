h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]

# Filtering the data if any "#" are existed in the each row or col
"""
Usage: 
filter(lambda row: <filtering condition>, grid or zip(*grid)) 
(Do not use if statement in <filtering condition> !)
If true, the row is not be deleted

"""
row_compressed_grid = list(filter(lambda row: any(x == "#" for x in row), grid))
compressed_grid = list(filter(lambda col: any(x == "#" for x in col), zip(*row_compressed_grid)))

# list -> string and out
"""
Note: 
when filtered by zip(*grid), the string order of the grid was transposed.
So the compressed grid should be zip(*compressed_grid) again.
"""
for row in zip(*compressed_grid):
    print("".join(row))