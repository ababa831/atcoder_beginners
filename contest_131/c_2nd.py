# AC
from fractions import gcd

A, B, C, D = map(int, input().split())

CD_lcm = (C * D) // gcd(C, D)


def divided(a, b, target):
    return b // target - (a - 1) // target


all_num = B - A + 1

div_t1 = divided(A, B, C)
div_t2 = divided(A, B, D)
div_extra = divided(A, B, CD_lcm)

print(all_num - div_t1 - div_t2 + div_extra)
