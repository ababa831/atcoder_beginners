N, M, X, Y = map(int, input().split())
x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))

# Judge "War" or "No War"
max_x = max(max(x_list), X)
min_y = min(min(y_list), Y)

if max_x < min_y:
    print("No War")
else:
    print("War")