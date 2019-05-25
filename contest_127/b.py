r, D, x_2000 = map(int, input().split())

x = x_2000
for _ in range(10):
    x = r * x - D
    print(x)