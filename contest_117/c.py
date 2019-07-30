# AC
N, M = map(int, input().split())

if N >= M:
    print(0)
    exit()

XXX = list(map(int, input().split()))
XXX.sort()

sections = [abs(XXX[i] - XXX[i + 1]) for i in range(M) if i < M - 1]
sections.sort(reverse=True)
not_arrived = sum(sections[:N-1])

print((XXX[-1] - XXX[0]) - not_arrived)
