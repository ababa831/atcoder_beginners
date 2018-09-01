k = int(input())
if k % 2 == 1:
    n_odd = int(k/2) + 1
    n_even = int(k/2)
else:
    n_odd = int(k/2)
    n_even = int(k/2)
print(n_odd*n_even)  