# Accepted
n_str = input()
n_int = int(n_str)
digits_sum = sum(list(map(int, list(n_str))))

if n_int % digits_sum:
    print("No")
else:
    print("Yes")