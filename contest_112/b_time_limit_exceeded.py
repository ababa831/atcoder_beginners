# Accepted
n, t = map(int, input().split())

c_list = []
t_list = []
min_c = 1000
n_append = 0
argmin_c = None
for _ in range(n):
    c_i, t_i = map(int, input().split())
    if t_i <= t:
        c_list.append(c_i)
        t_list.append(t_i)
        n_append += 1
        if min_c >= c_i:
            min_c = c_i
            argmin_c = len(c_list) - 1 

if n_append > 0:
    print(c_list[argmin_c])
else:
    print("TLE")