# Accepted
n = int(input())
k = int(input())

x = 1
for i in range(n):
    tmp_twiced = 2 * x
    tmp_plus_k = x + k
    if tmp_twiced <= tmp_plus_k:
        x = tmp_twiced
    else:
        x = tmp_plus_k

print(x)