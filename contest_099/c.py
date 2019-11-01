# WIP（The fucking code）
from math import log
N = int(input())


def search_range(target_yen, remaining):
    x = 1
    log_value = log(target_yen)
    log_n = log(remaining)
    while log_n > log_value:
        x += 1
        log_value = x * log(target_yen)
    return x - 1, x


def get_selected_power(idx_canditate, power_9, power_6):
    if idx_canditate == 0:
        return power_9
    elif idx_canditate == 1:
        return power_6
    else:
        return 1


n_operation = 0
remaining = N
while remaining > 0:
    power_9, _ = search_range(6, remaining)
    power_6, _ = search_range(9, remaining)
    canditate = [9**power_9, 6**power_6, 1]
    sub_number = max([9**power_9, 6**power_6, 1])
    idx_cand = canditate.index(sub_number)
    selected_power = get_selected_power(idx_cand, power_9, power_6)
    if selected_power == 0:
        selected_power = 1

    remaining -= sub_number
    n_operation += selected_power

print(n_operation)
