# Accepted
s_list = list(input())
t_list = list(input())
n_oneroop = len(s_list)

for _ in range(n_oneroop):
    s_list = [s_list[-1]] + s_list[:-1]
    if s_list == t_list:
        print("Yes")
        exit()
print("No")

# A sample answer
"""
s = input()
print('Yes' if input() in s + s else 'No')
"""