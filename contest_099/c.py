# WIP (The fucking code)
N = int(input())


def search_range(target_yen, remaining):
    x = 1
    exp_val = target_yen ** x
    while remaining > exp_val:
        x += 1
        exp_val = target_yen ** x
    return x - 1


n_operation = 0
remaining = N
inf = float('inf')
while remaining > 0:
    power_9 = search_range(9, remaining)
    power_6 = search_range(6, remaining)
    canditate = None
    if power_9 == 0 and power_6 == 0:
        canditate = [inf, inf, remaining]
    elif power_9 == 0:
        canditate = [inf, remaining - 6**power_6, remaining]
    elif power_6 == 0:
        canditate = [remaining - 9**power_9, inf, remaining]
    else:
        canditate = [remaining - 9**power_9, remaining - 6**power_6, remaining]

    # Update remaining
    remaining = min(canditate)
    argmin_cand = canditate.index(remaining)
    target_power = remaining if argmin_cand == 2 else 1
    # print(canditate, argmin_cand, target_power, remaining)
    n_operation += target_power
    if argmin_cand == 2:
        break

# print('========')
print(n_operation)
