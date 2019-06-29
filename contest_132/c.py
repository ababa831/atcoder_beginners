# AC
N = int(input())
ddd = list(map(int, input().split()))

ddd = sorted(ddd)

ddd_mid1 = ddd[N // 2 - 1]
ddd_mid2 = ddd[N // 2]
print(ddd_mid2 - ddd_mid1)
