# Accepted
import math
n = int(input())
p_list = list(map(int, [input() for _ in range(n)]))

max_p = max(p_list)
argmax_p = p_list.index(max_p)
discount_price = int(max_p / 2)
p_list[argmax_p] = discount_price
total_price = sum(p_list)

print(total_price)