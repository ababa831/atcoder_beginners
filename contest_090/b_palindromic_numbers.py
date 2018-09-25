# Accepted
"""
10000 <= A <= B <= 99999

So, constraints are as follows:
- 10000 digit = 1 digit
- 1000 digit = 10 digit
(You can choose 0~9 arbitrarily because 100 digit is centered.)

---
O(n)
max(n) = 90000
A little bit slow algorithm, but ignoreable.
"""
a, b = map(int, input().split())

n_satisfied = 0
for i in range(a, b + 1):
    i_str = str(i)
    if i_str[0] == i_str[4] and i_str[1] == i_str[3]:
        n_satisfied += 1

print(n_satisfied)

# Another answer
"""
Note that symmetry with
- 10000, 1 digits
- 1000, 10 digits

->

for <10000 or 1 digits value> in range(10):
    for <1000 or 10 digits value> in range(10):
        for <100 digit value> in range(10):
            ...

Therefore, Complexity of the algorithm is 3/5 of the former one.
"""
"""
a, b = map(int, input().split())

n_satisfied = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            c = 10000 * i + 1000 * j + 100 * k + 10 * j + i
            if a <= c <= b:
                n_satisfied += 1

print(n_satisfied)
"""