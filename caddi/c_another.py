# WA (the last test case only)
n, p = map(int, input().split())

max_canditate = int(p**(1. / n))
for cand in range(max_canditate, 0, -1):
    if p % (cand ** n) == 0:
        # max_cand^n * ? = p was found -> cand is GCD
        print(cand)
        exit()
