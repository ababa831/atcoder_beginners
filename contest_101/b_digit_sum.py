# Accepted
n_str = input()
n_int = int(n_str)
digit_sum = sum([int(digit) for digit in list(n_str)])
if n_int % digit_sum == 0:
    print("Yes")
else:
    print("No")