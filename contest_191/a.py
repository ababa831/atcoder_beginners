v, t, s, d = map(int, input().split())

if t*v <= d <= s*v:
    print('No')
else:
    print('Yes')