# TLE
# Commentary: https://img.atcoder.jp/agc028/editorial.pdf
from fractions import gcd
import copy

alphabet = [chr(i) for i in range(97, 97 + 26)]


def lcm(x, y):
    return (x * y) // gcd(x, y)


# Input data
n, m = map(int, input().split())
s = input()
t = input()

# Generate x canditate
x_len = lcm(n, m)
canditates_s = ["" for i in range(x_len)]
# NG(Call by reference)：canditates_t = canditates_s
canditates_t = copy.copy(canditates_s)
s_indlist = [i * int(x_len / n) for i in range(n)]
t_indlist = [i * int(x_len / m) for i in range(m)]
for i, s_ind in enumerate(s_indlist):
    canditates_s[s_ind] = s[i]
for i, t_ind in enumerate(t_indlist):
    canditates_t[t_ind] = t[i]

# Shared set
shared_set = set(s_indlist) & set(t_indlist)

# Djudge incoherence
for i in shared_set:
    if canditates_s[i] != canditates_t[i]:
        print(-1)
        exit()

# If the djudge cleared
print(x_len)