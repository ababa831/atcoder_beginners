# Accepted
n, m, a, b = map(int, input().split())

val_a_mikans = []
for i in range(m):
    l_i, r_i = map(int, input().split())
    val_a_mikans += [j for j in range(l_i, r_i + 1)]
num_val_a = len(set(val_a_mikans))
num_val_b = n - num_val_a

print(a * num_val_a + b * num_val_b)