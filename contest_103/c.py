"""[summary]
Simple search
-> Complexity: 10**5 * 3000
-> TLE

Need to find a solution with less complexity
"""
# May be TLE
from fractions import gcd
import sys


def lcm(x, y):
    return (x * y) // gcd(x, y)

# Input
N = input()
aaa = list(map(int, sys.stdin.readline().split()))

# Solve total LCM
total_lcm = 1
for a in aaa:
    total_lcm = lcm(total_lcm, a)

# Find max f(m)
max_f = 0
for m_canditate in range(1, total_lcm+1):
    f = 0
    for a in aaa:
        f += 