# Wrong answer at sight
# I coudn't find out algorithm of alternate selections.
# I ignored the description "両者が最大の数値とろうとする".
import numpy as np

n = int(input())
a_list = list(map(int, input().split()))

n_alice = 0
n_bob = 0

for i in range(1, n+1):
    if i % 2:
        n_alice += max(a_list)
        del a_list[np.argmax(a_list)]
    else:
        n_bob += min(a_list)
        del a_list[np.argmin(a_list)]

print(n_alice - n_bob)

# Model answer
# 1. Sort a_list DESC
# 2. Use slice　[start:end:increment]
n = int(input())
a_list = sorted(list(map(int, input().split())), reverse=True)
n_alice = sum(a_list[::2])
n_bob = sum(a_list[1::2])
print(n_alice - n_bob)




