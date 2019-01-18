# Accepted
n = int(input())
a, b = map(int, input().split())
p_list = list(map(int, input().split()))

len_p_over_a = len([p_i for p_i in p_list if p_i <= a])
len_p_ap1_to_b = len([p_i for p_i in p_list if a+1 <= p_i <= b])
len_p_over_bp1 = len([p_i for p_i in p_list if b+1 <= p_i])

min_combi = min(len_p_over_a, len_p_ap1_to_b, len_p_over_bp1)
print(min_combi)
