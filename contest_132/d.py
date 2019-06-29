from math import factorial

N, K = map(int, input().split())
MOD = 10**9 + 7


def calc_conbi(a, b):
    if b == 0 or b == a:
        return 1
    elif b == 1:
        return a
    else:
        nume = factorial(a) // factorial(b - 1)
        deno = factorial(b)
    return nume // deno


for i in range(1, K + 1):
    combi_select_spot = calc_conbi(N - K + 1, i)
    combi_remain = calc_conbi(K - 1, i - 1)
    print(combi_select_spot * combi_remain % MOD)
