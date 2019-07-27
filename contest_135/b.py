# AC
from copy import deepcopy
from itertools import combinations


N = int(input())
ppp = list(map(int, input().split()))
ppp_sorted = sorted(ppp)

combis = list(combinations(ppp, 2))

if ppp == ppp_sorted:
    print('YES')
    exit()
if N == 2:
    print('YES')
    exit()

for combi in combis:
    i = ppp.index(combi[0])
    j = ppp.index(combi[1])
    ppp_copy = deepcopy(ppp)
    ppp_copy[i], ppp_copy[j] = ppp[j], ppp[i]
    if ppp_copy == ppp_sorted:
        print('YES')
        exit()

print('NO')
