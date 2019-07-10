# AC
from fractions import gcd

N = int(input())
AAA = list(map(int, input().split()))

dp_l = [0] * (N + 1)
dp_r = [0] * (N + 1)

dp_l[0] = 0
dp_r[0] = 0

for i in range(1, N):
    dp_l[i] = gcd(dp_l[i - 1], AAA[i - 1])
    dp_r[i] = gcd(dp_r[i - 1], AAA[-i])

max_gcd = 0
for i in range(N + 1):
    gcd_cand = gcd(dp_l[i], dp_r[N - i - 1])
    max_gcd = max(gcd_cand, max_gcd)

print(max_gcd)
