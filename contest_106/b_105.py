# Accepted
n = int(input())
odds = [val for val in range(1, n+1) if val % 2 == 1]

n_eight_devisor = 0
for odd in odds:
    n_divisor = 0
    # Count number of divisor
    for i in range(1, odd+1):
        if odd % i == 0:
            n_divisor += 1
    if n_divisor == 8:
        n_eight_devisor += 1

print(n_eight_devisor)