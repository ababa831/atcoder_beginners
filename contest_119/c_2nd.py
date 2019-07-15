"""
Give up: 
    I could not find out how to deal with
    the operations of after concatnation.
"""

N, A, B, C = map(int, input().split())
lll = [int(input()) for _ in range(N)]

# Three DPs
max_trial = 1000
dp_ext = [[(0, 0) for _ in range(N)]] * max_trial
dp_shr = [[(0, 0) for _ in range(N)]] * max_trial
dp_conc = [[(0, 0) for _ in range(N)]] * max_trial

# Initialize
dp_ext[0] = [(l, 0) for l in lll]
dp_shr[0] = [(l, 0) for l in lll]
dp_conc[0] = [(l, 0) for l in lll]

for i in range(max_trial - 1):
    zip_last = zip(dp_ext[i], dp_shr[i], dp_conc[i])
    for j, lmp_3methods in enumerate(zip_last):
        # Select lowest MP for time i 
        min_method = min(lmp_3methods, key=lambda x: x[1])
        # For "shrink" method
        lmp_3methods_for_shr = [lmp for lmp in lmp_3methods if lmp[0] > 1]
        min_method_shr = min(lmp_3methods_for_shr, key=lambda x: x[1])
            
        dp_ext[i + 1][j] = (min_method[0] + 1, min_method[1] + 1)
        dp_shr[i + 1][j] = (min_method_shr[0] - 1, min_method_shr[1] + 1)
        dp_conc[i + 1][j] = (min_method[0] * 1, min_method[1] + 1)

