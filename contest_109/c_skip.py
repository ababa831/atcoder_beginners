# Wrong answer
# Learn Euclidean Algorithm!
N, X = map(int, input().split())
x_list = list(map(int, input().split()))
x_list.append(X)

x_list = sorted(x_list)
if N == 1:
    min_diff = x_list[1] - x_list[0]
else:
    x_diffs = [val - x_list[i - 1] for i, val in enumerate(x_list) if i > 0]
    min_diff = min(x_diffs)
D_canditates = [i for i in range(1, min_diff + 1) if min_diff % i == 0]

# Search max D
D_list = []
for D_cand in D_canditates:
    for x_diff in x_diffs:
        if x_diff % D_cand == 0:
            D_list.append(D_cand)
print(min(D_list))