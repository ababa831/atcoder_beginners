# Review of a simple bit search algorithm
D = 3
print('Number of digit', D)

combinations = []
for i in range(1 << D):
    flaged = []
    for j in range(D):
        if (i >> j) & 1:
            flaged.append(j + 1)
    print('Binary {} has flags at digit {}'.format(bin(i), flaged))
    combinations.append(flaged)

print('Total number of combinations ', len(combinations))
print('Combinations: ', combinations)
