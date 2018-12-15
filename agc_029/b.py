# WA and TLE
import itertools

# Prepareation
splitters = [
    2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384,
    32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608,
    16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824
]

n = int(input())
a_list = list(map(int, input().split()))

a_combis = itertools.combinations(a_list, 2)
n_2powered = 0
for combi in a_combis:
    sum_combi = sum(combi)
    if sum_combi in splitters:
        n_2powered += 1

print(n_2powered)