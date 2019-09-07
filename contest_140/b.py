# AC
import sys
input = sys.stdin.readline

N = int(input())
AAA = list(map(int, input().split()))
BBB = list(map(int, input().split()))
CCC = list(map(int, input().split()))

n_satisfy = 0
for i, A in enumerate(AAA):
    B = BBB[A - 1]
    if i == 0:
        n_satisfy += B
    elif AAA[i - 1] + 1 != A:
        n_satisfy += B
    else:
        n_satisfy += B + CCC[A - 1 - 1]

print(n_satisfy)
