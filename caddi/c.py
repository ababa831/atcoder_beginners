# WA (the last test case only)
from fractions import gcd


n, p = map(int, input().split())

if p == 1:
    print(1)
elif n == 1:
    print(p)
else:
    max_canditate = int(p**(1. / n))
    if p % (max_canditate ** n) == 0:
        print(max_canditate)
    else:
        for cand in range(max_canditate, 0, -1):
            if p % (cand ** n) == 0:
                extra_splitter = p / (cand ** n)
                # max_cand^n * ? = p was found -> GCD(max_cand, extra_splitter)
                num_gcded = gcd(max_canditate, extra_splitter)
                print(cand)
                exit()
