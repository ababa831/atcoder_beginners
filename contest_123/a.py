# Accepted
import itertools

antenas = list(map(int, [input() for _ in range(5)]))
k = int(input())
c_list = list(itertools.combinations(antenas, 2))

for combi in c_list:
    length = abs(combi[0] - combi[1])
    if length > k:
        print(':(')
        exit()
print('Yay!')
