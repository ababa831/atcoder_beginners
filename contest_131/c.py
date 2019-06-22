# Runtime Error (Only one case failed)
from fractions import gcd

A, B, C, D = map(int, input().split())

CD_lcm = C * D // gcd(C, D)

n_cant_divs = []
for target in [C, D, CD_lcm]:
    if B < target:
        n_cant_divs.append(A - B + 1)
    if A <= target <= B:
        t_cant_div = target - A
        can_div = B // target
        t_cant_div2 = (B - target + 1) - can_div
        n_cant_divs.append(t_cant_div + t_cant_div2)
    elif target < A:
        can_div_w_over = B // target
        correction = (A - 1) // target
        actual_can_div = can_div_w_over - correction
        t_cant_div = (B - A + 1) - actual_can_div
        n_cant_divs.append(t_cant_div)

print(n_cant_divs[0] + n_cant_divs[1] - n_cant_divs[2])
