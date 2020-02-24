# AC (Another answer)
N = int(input())
AAA = list(map(int, input().split()))
AAA = sorted(AAA)

last_A = None
for A in AAA:
    if A == last_A:
        print('NO')
        exit()
    last_A = A
print('YES')
