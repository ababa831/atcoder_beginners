# WIP
N_str = input()
len_N = len(N_str)
N = int(N_str)

# [is_max][7_appeared][5_appeared][3_appeared]
dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(N)]
