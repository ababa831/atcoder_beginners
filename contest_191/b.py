N, X = map(int, input().split())
AAA = list(map(int, input().split()))

AAA_d = []
for A in AAA:
    if X != A:
        AAA_d.append(str(A))

print(' '.join(AAA_d))