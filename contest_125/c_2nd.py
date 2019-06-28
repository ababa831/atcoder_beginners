# AC
from fractions import gcd

N = int(input())
AAA = list(map(int, input().split()))

# DP
dp_l = [0] * (N + 1)
dp_r = [0] * (N + 1)
for i in range(1, N):
    dp_l[i] = gcd(dp_l[i - 1], AAA[i-1])
    dp_r[i] = gcd(dp_r[i - 1], AAA[-i])

# Get max gcd for all combinations
max_m = -1
for i in range(N+1):
    m = gcd(dp_l[i], dp_r[N-i-1])
    max_m = max(max_m, m)
print(max_m)
