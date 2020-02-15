# AC
N, M = map(int, input().split())

if N == 1 and M == 1:
    print(1)
elif N == 1:
    print(M - 2 if M > 2 else 0)
elif M == 1:
    print(N - 2 if N > 2 else 0)
elif N > 2 and M > 2:
    print((N - 2) * (M - 2))
else:
    print(0)
