# 途中
n, x = map(int, input().split())
a_list = sorted(list(map(int, input().split())))

n_children = 0
for a in a_list:
    # if x < min(a_list)
    if x < a:
        break
    else:
        x -= a
        n_children += 1

print(n_children)