# 初見正解
# How to extract no duplicated list
# -> Use set() to convert list
n = int(input())
d_list = sorted(list(map(int, set([input() for _ in range(n)]))), reverse=True)
print(len(d_list))


