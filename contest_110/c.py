# AC
import sys
input = sys.stdin.readline

S = input().replace('\n', '')
T = input().replace('\n', '')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
len_alphabet = len(alphabet)
dict_alphabet = {chara: i for i, chara in enumerate(alphabet)}


def calc_state(target_string):
    state_idx = [[] for _ in range(len_alphabet)]
    state_count = [0 for _ in range(len_alphabet)]

    for i, chara in enumerate(target_string):
        alphabet_idx = dict_alphabet[chara]
        state_idx[alphabet_idx].append(i)
        state_count[alphabet_idx] += 1

    return state_idx, state_count


state_idx_s, state_count_s = calc_state(S)
state_idx_t, state_count_t = calc_state(T)


if sorted(state_count_s) != sorted(state_count_t):
    print('No')
    exit()

# If the same alphabet appears twice in succession in S,
# does the same law occurs in T?
last_s = None
last_t = None
for s, t in zip(S, T):
    if last_s == s and last_t != t:
        print('No')
        exit()
    last_s, last_t = s, t

print('Yes')
