# AC
N = int(input())
AAA = list(map(int, input().split()))

appeared = set([])

for A in AAA:
    if A in appeared:
        print('NO')
        exit()
    appeared.add(A)

print('YES')
