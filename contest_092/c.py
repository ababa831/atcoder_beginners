# AC, a complexity of the problem is not so large
import sys
sys_input = sys.stdin.readline

N = int(input())
AAA = list(map(int, sys_input().split()))
AAA = [0] + AAA + [0]

basic_cost = sum([abs(AAA[i + 1] - A) for i, A in enumerate(AAA[:N + 1])])

for i, A in enumerate(AAA[:N + 1]):
    if i == 0:
        continue
    adjusted_cost = basic_cost - abs(A - AAA[i-1]) - abs(A - AAA[i+1]) \
        + abs(AAA[i+1]-AAA[i-1])
    print(adjusted_cost)
