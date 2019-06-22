# AC
N = int(input())
ABs = [tuple(map(int, input().split())) for _ in range(N)]
ABs = sorted(ABs, key=lambda x: x[1])

elapsed_time = 0
for AB in ABs:
    A = AB[0]
    B = AB[1]
    if elapsed_time + A > B:
        print('No')
        exit()
    elapsed_time += A

print('Yes')
