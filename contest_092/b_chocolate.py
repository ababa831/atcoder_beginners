# Accepted
n = int(input())
d, x = map(int, input().split())
a_list = list(map(int, [input() for _ in range(n)]))

n_eaten = 0
for a_i in a_list:
    k = 0
    while k * a_i + 1 <= d:
        n_eaten += 1
        k += 1

print(n_eaten + x)