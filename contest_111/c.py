# AC
import sys
input = sys.stdin.readline

N = int(input())
vvv = list(map(int, input().split()))

if len(set(vvv)) == 1:
    print(N // 2)
    exit()

vvv_odd = vvv[::2]
vvv_even = vvv[1::2]

dp_odd = [0] * max(vvv_odd)
dp_even = [0] * max(vvv_even)

for v_odd, v_even in zip(vvv_odd, vvv_even):
    dp_odd[v_odd - 1] += 1
    dp_even[v_even - 1] += 1

max_appear_odd = max(dp_odd)
max_appear_even = max(dp_even)

max_odd_val = dp_odd.index(max_appear_odd) + 1
max_even_val = dp_even.index(max_appear_even) + 1

if max_odd_val == max_even_val:
    next_appear_odd = sorted(dp_odd, reverse=True)[1]
    next_appear_even = sorted(dp_even, reverse=True)[1]
    if next_appear_odd > next_appear_even:
        max_appear_odd = next_appear_odd
    else:
        max_appear_even = next_appear_even

n_replace = N // 2 - max_appear_odd
n_replace += N // 2 - max_appear_even

print(n_replace)
