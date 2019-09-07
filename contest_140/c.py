# AC
N = int(input())
BBB = list(map(int, input().split()))
BBB += [10**5]

AAA = [0] * N

AAA[0] = BBB[0]

for i, B in enumerate(BBB[:-1]):
    AAA[i + 1] = min(B, BBB[i + 1])

print(sum(AAA))
