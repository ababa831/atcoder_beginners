n = int(input())
ppp = list(map(int, input().split()))

n_satisfy_cond = 0
for i in range(1, n - 1):
    p_im1 = ppp[i - 1]
    p_i = ppp[i]
    p_ip1 = ppp[i + 1]
    if p_im1 < p_i < p_ip1:
        n_satisfy_cond += 1
    elif p_ip1 < p_i < p_im1:
        n_satisfy_cond += 1

print(n_satisfy_cond)
