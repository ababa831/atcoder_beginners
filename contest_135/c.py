# AC: the fucking code
from copy import copy

N = int(input())
AAA = list(map(int, input().split()))
BBB = list(map(int, input().split()))

n_defeated = 0
for idx, (A, B) in enumerate(zip(AAA[:N + 1], BBB)):
    A = AAA[idx]
    Ap1 = AAA[idx + 1]
    mp_b = copy(B)
    # print('0:',AAA, mp_b)
    # position i
    if A > B:
        n_defeated += B
        AAA[idx] -= B
        mp_b = 0
    else:
        n_defeated += A
        AAA[idx] = 0
        mp_b = B - A
    # position i+1
    # print('1:',AAA, mp_b)
    if Ap1 > mp_b:
        n_defeated += mp_b
        AAA[idx + 1] -= mp_b
        mp_b = 0
    else:
        n_defeated += Ap1
        AAA[idx + 1] = 0
        mp_b -= Ap1
    # print('2:',AAA, mp_b)

print(n_defeated)