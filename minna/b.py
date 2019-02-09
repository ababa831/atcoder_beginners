# Accepted
# There are 3 paths, four cities
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())

patterns = [[(a1, a2, a3), (b1, b2, b3)],
            [(b1, a2, a3), (a1, b2, b3)],
            [(a1, b2, a3), (b1, a2, b3)],
            [(a1, a2, b3), (b1, b2, a3)],
            [(b1, b2, a3), (a1, a2, b3)],
            [(b1, a2, b3), (a1, b2, a3)],
            [(a1, b2, b3), (b1, a2, a3)],
            [(b1, b2, b3), (a1, a2, a3)]]

for pattern in patterns:
    set1 = set(pattern[0])
    set2 = set(pattern[1])
    if len(set1) == 3 and len(set2) == 3:
        print('YES')
        exit()

print('NO')