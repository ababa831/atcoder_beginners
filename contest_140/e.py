# Should be TLE
import sys
input = sys.stdin.readline

N = int(input())
PPP = list(map(int, input().split()))

total = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        PPP_sorted = sorted(PPP[i:j + 1], reverse=True)
        total += PPP_sorted[1]

print(total)
