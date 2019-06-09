N = int(input())
Wlist = list(map(int, input().split()))

min_diff = 10000000000
for t in range(N):
    S1 = sum(Wlist[:t + 1])
    S2 = sum(Wlist[t + 1:])
    min_diff = min(min_diff, abs(S2 - S1))

print(min_diff)