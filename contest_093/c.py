# AC, (Careless mistake)
A, B, C = map(int, input().split())

combi = [A, B, C]
set_abc = set(combi)

len_set_abc = len(set_abc)
max_set = max(set_abc)
min_set = min(set_abc)
if len_set_abc == 1:
    print(0)
elif len_set_abc == 2:
    max_freq = combi.count(max_set)
    diff = max_set - min_set
    if max_freq == 2 and diff % 2:
        print((diff + 1) // 2 + 1)
    elif max_freq == 2:
        print(diff // 2)
    else:
        print(diff)
else:
    other = [c for c in combi if c != max_set]
    max_other = max(other)
    min_other = min(other)

    n_operation = max_set - max_other
    max_other += n_operation
    min_other += n_operation

    diff = max_set - min_other

    if diff % 2:
        n_add = (max_set - min_other) // 2 + 2
    else:
        n_add = (max_set - min_other) // 2
    n_operation += n_add

    print(n_operation)
