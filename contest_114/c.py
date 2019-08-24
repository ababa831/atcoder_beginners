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
    dp3[0][0] = 1
    dp3[0][1] = 0
    dp5[0][0] = 1
    dp5[0][1] = 0
    dp7[0][0] = 1
    dp7[0][1] = 0
    dp35[0][0] = 2
    dp35[0][1] = 0
    dp57[0][0] = 2
    dp57[0][1] = 0
    dp73[0][0] = 2
    dp73[0][1] = 0
elif d_0 == 7:
    dp_all[0][0] = 2
    dp_all[0][1] = 1
    dp3[0][0] = 0
    dp3[0][1] = 0
    dp5[0][0] = 0
    dp5[0][1] = 0
    dp7[0][0] = 0
    dp7[0][1] = 1
    dp35[0][0] = 0
    dp35[0][1] = 0
    dp57[0][0] = 0
    dp57[0][1] = 1
    dp73[0][0] = 0
    dp73[0][1] = 1
elif 7 > d_0 > 5:
    dp_all[0][0] = 2
    dp_all[0][1] = 0
    dp3[0][0] = 1
    dp3[0][1] = 0
    dp5[0][0] = 1
    dp5[0][1] = 0
    dp7[0][0] = 0
    dp7[0][1] = 0
    dp35[0][0] = 2
    dp35[0][1] = 0
    dp57[0][0] = 1
    dp57[0][1] = 0
    dp73[0][0] = 1
    dp73[0][1] = 0
elif d_0 == 5:
    dp_all[0][0] = 1
    dp_all[0][1] = 1
    dp3[0][0] = 1
    dp3[0][1] = 0
    dp5[0][0] = 0
    dp5[0][1] = 1
    dp7[0][0] = 0
    dp7[0][1] = 0
    dp35[0][0] = 1
    dp35[0][1] = 1
    dp57[0][0] = 0
    dp57[0][1] = 1
    dp73[0][0] = 1
    dp73[0][1] = 0
elif 5 > d_0 > 3:
    dp_all[0][0] = 1
    dp_all[0][1] = 0
    dp3[0][0] = 1
    dp3[0][1] = 0
    dp5[0][0] = 0
    dp5[0][1] = 0
    dp7[0][0] = 0
    dp7[0][1] = 0
    dp35[0][0] = 1
    dp35[0][1] = 0
    dp57[0][0] = 0
    dp57[0][1] = 0
    dp73[0][0] = 1
    dp73[0][1] = 0
elif d_0 == 3:
    dp_all[0][0] = 0
    dp_all[0][1] = 1
    dp3[0][0] = 0
    dp3[0][1] = 1
    dp5[0][0] = 0
    dp5[0][1] = 0
    dp7[0][0] = 0
    dp7[0][1] = 0
    dp35[0][0] = 0
    dp35[0][1] = 1
    dp57[0][0] = 0
    dp57[0][1] = 0
    dp73[0][0] = 0
    dp73[0][1] = 1

for i, (dpv_all, dpv3, dpv5, dpv7, dpv35, dpv57,
        dpv73) in zip(dp_all, dp3, dp5, dp7, dp35, dp57, dp73):
    # TODO: code dp equations for i
    pass
