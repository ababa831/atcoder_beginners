# Accepted
n = int(input())
for n_cake in range(n):
    for n_donut in range(n):
        if 4 * n_cake + 7 * n_donut == n:
            print("Yes")
            exit()
print("No")