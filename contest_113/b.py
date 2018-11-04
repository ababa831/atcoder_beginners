# Accepted
n = int(input())
t, a = map(int, input().split())
h_list = map(int, input().split())

min_tempdiff = 10000  # 十分大きい値で！
argmin_tempdiff = None
for i, h_val in enumerate(h_list):
    temp_diff = abs(a - (t - h_val * 0.006))
    if min_tempdiff > temp_diff:
        min_tempdiff = temp_diff
        argmin_tempdiff = i + 1  # 地点は配列インデックス+1

print(argmin_tempdiff)