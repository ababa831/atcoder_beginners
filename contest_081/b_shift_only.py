# Accepted
n = int(input())
a_list = list(map(int, input().split()))

n_division = 0
while True:
    a_list = [a/2 for a in a_list if a % 2 == 0]
    if len(a_list) != n:
        print(n_division)
        exit()
    else:
        n_division += 1