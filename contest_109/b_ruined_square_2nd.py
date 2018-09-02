x1, y1, x2, y2 = map(int, input().split())

x_diff = x1 - x2
y_diff = y2 - y1

x4 = x1 - y_diff
y4 = y1 - x_diff
x3 = x2 - y_diff
y3 = y2 - x_diff

print(x3, y3, x4, y4)