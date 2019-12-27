A, B, C = map(int, input().split())

combi = [A, B, C]
max_ABC = max([A, B, C])
other = [c for c in combi if c != max_ABC]
max_other = max(other)
min_other = min(other)

# Operation (1st method)
n_operation = max_ABC - max_other
max_other += n_operation
min_other += n_operation

# Operation (2nd method)
if (max_ABC - min_other) % 2:
    n_add = (max_ABC - min_other) // 2 + 1
else:
    n_add = (max_ABC - min_other) // 2
n_operation += n_add

print(n_operation)
