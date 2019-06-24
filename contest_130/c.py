W, H, x, y = map(int, input().split())

s = W * H / 2
if 2 * x == W and 2 * y == H:
    print(s, 1)
else:
    print(s, 0)
