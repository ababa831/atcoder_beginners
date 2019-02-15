abcd = input()

answer = 0
for i in range(1 << len(abcd) - 1):
    formula = abcd[0]
    for j in range(len(abcd) - 1):
        if (i >> j) & 1:
            formula += '+'
        else:
            formula += '-'
        formula += abcd[j + 1]
    canditate = eval(formula)
    if canditate == 7:
        print(formula + '=7')
        exit()