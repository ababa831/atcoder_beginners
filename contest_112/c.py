# Gave up
n = int(input())

if n == 1:
    Cx, Cy, H = map(int, input().split())
    print(Cx, Cy, H)
elif n == 2:
    x_1, y_1, h_1 = map(int, input().split())
    x_2, y_2, h_2 = map(int, input().split())
    if h_1 >= h_2:
        print(x_1, y_1, h_1)
    else:
        print(x_2, y_2, h_2)