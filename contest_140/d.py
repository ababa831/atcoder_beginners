# WIP (May be WA)
import sys
input = sys.stdin.readline

N, K = map(int, input())
S = input()

target_char = 'R' if S[0] == 'L' else 'L'

max_happiness = 0
for l in range(1, N):
    tmp_max = 0
    tmpstate_max = ''
    for r in range(l, N):
        s_selected = S[l:r + 1]
        tmp_val = S[l:r + 1].count(target_char)
        if tmp_max < tmp_val:
            tmp_max = tmp_val
            tmpstate_max = s_selected
            # WIP
