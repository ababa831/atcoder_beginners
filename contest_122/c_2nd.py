# AC
N, Q = map(int, input().split())
S = input()

ac_counts = [0] * N
last = ''
n_count = 0
for idx, current in enumerate(S):
    if last == 'A' and current == 'C':
        n_count += 1
        ac_counts[idx] = n_count
    elif idx != 0:
        ac_counts[idx] = ac_counts[idx - 1]
    last = current

for _ in range(Q):
    l, r = map(int, input().split())
    print(ac_counts[r - 1] - ac_counts[l - 1])
