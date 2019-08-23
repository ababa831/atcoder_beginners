# WIP
N_str = input()
len_N = len(N_str)
N = int(N_str)

# dp
dp_all = [[-1, -1] for _ in range(len_N)]
dp3 = [[-1, -1] for _ in range(len_N)]
dp5 = [[-1, -1] for _ in range(len_N)]
dp7 = [[-1, -1] for _ in range(len_N)]
dp35 = [[-1, -1] for _ in range(len_N)]
dp57 = [[-1, -1] for _ in range(len_N)]
dp73 = [[-1, -1] for _ in range(len_N)]

d_0 = int(N_str[0])
if d_0 > 7:
    dp_all[0][0] = 3
    dp_all[0][1] = 0
    # TODO: code other dps
elif d_0 == 7:
    dp_all[0][0] = 2
    dp_all[0][1] = 1
elif 7 > d_0 > 5:
    dp_all[0][0] = 2
    dp_all[0][1] = 0
elif d_0 == 5:
    dp_all[0][0] = 1
    dp_all[0][1] = 1
elif 5 > d_0 > 3:
    dp_all[0][0] = 1
    dp_all[0][1] = 0
elif d_0 == 3:
    dp_all[0][0] = 0
    dp_all[0][1] = 1

