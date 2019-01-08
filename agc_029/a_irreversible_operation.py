# Accepted
s = input()
 
is_all_swappd = False
n_swap = 0
n_white = s.count('W')
for i in range(n_white):
    w_idx = None
    if i == 0:
        w_idx = s.find('W')
    else:
        w_idx = s[last_w_idx + 1:].find('W') + last_w_idx + 1
    n_swap += w_idx - i
    last_w_idx = w_idx
 
print(n_swap)
