# Accepted
n, m, c = map(int, input().split())
b_list = list(map(int, input().split()))

n_correct = 0
for i in range(n):
    sum_eq = sum(
        [a * b_list[j] for j, a in enumerate(list(map(int,
                                                      input().split())))])
    if sum_eq + c > 0:
        n_correct += 1
print(n_correct)