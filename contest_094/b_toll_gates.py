# Accepted
n, m, x = map(int, input().split())
a_list = list(map(int, input().split()))

left_a_list = [a for a in a_list if a < x]
right_a_list = [a for a in a_list if a > x]
min_cost = min(len(left_a_list), len(right_a_list))

print(min_cost)