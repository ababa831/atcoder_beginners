# Accepted
n, m = map(int, input().split())

a_b_list = []
for i in range(n):
    a, b = map(int, input().split())
    a_b_list.append({'yen':a, 'n_drink':b})
a_b_list.sort(key=lambda x: x['yen'])

n_leftover = m
yen_spent = 0
for i in range(n):
    n_drink = a_b_list[i]['n_drink']
    yen = a_b_list[i]['yen']
    if a_b_list[i]['n_drink'] < n_leftover:
        yen_spent += n_drink * yen
        n_leftover -= n_drink
    else:
        yen_spent += n_leftover * yen
        print(yen_spent)
        exit()