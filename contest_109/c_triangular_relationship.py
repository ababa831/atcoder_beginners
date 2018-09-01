# This is a wrong answer
n, k = map(int, input().split())
n_division = 0
# a=b=c
n_division += sum([1 for i in range(1, n+1) if 2 * i % k == 0])
# a=b!=c
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if 2 * i % k == 0 and (i + j) % k == 0:
            n_division += 3 # x 3 patters
# a!=b!=c
for i in range(1, n+1):
    for j in range(i+1, n+1):
        for l in range(j+1, n+1):
            if (i + j) % k == 0 and (j + l) % k == 0 and (l + i) % k == 0:
                n_division += 6 # x 6 patters
print(n_division)