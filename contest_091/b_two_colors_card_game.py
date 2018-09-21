# Accepted
n = int(input())
s_list = [input() for _ in range(n)]
m = int(input())
t_list = [input() for _ in range(m)]

max_profit = -100  # M <= 100 -> max_profit is larger than -100
canditates = set(s_list)
for canditate in canditates:
    tmp_profit = s_list.count(canditate) - t_list.count(canditate)
    if tmp_profit > max_profit:
        max_profit = tmp_profit   
print(max(max_profit, 0))  # output > 0