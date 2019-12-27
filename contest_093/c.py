A, B, C = map(int, input().split())

if A == B == C:
    print(0)
    exit()

combi = [A, B, C]
max_ABC = max([A, B, C])
other = [c for c in combi if c != max_ABC]
max_other = max(other)
min_other = min(other)

# Operation (1st method)
n_operation = max_ABC - max_other
max_other += n_operation
min_other += n_operation

if max_other == min_other:
    print(n_operation)
    exit()

# Operation (2nd method)
diff = max_ABC - min_other
if diff % 2 and diff == 1:
    n_add = (max_ABC - min_other) // 2 + 2
elif diff % 2:
    n_add = (max_ABC - min_other) // 2 + 1
else:
    n_add = (max_ABC - min_other) // 2
n_operation += n_add

print(n_operation)
