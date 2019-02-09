n, k = map(int, input().split())

s = n % 2
q = int(n / 2)

if s:
    if k <= q + s:
        print('YES')
    else:
        print('NO')
else:
    if k <= q:
        print('YES')
    else:
        print('NO')
    