# WIP
import sys
sys_input = sys.stdin.readline

N = int(input())
AAA = list(map(int, sys_input().split()))

# Get index when pos/neg number changed to neg/pos
last_positive = None
sep_indices = []
max_absvals = []
argmaxes = []
second_absvals = []
arg2nds = []
max_absval = AAA[0]
argmax = 0
second_absval = None
arg2nd = None
for i, A in enumerate(AAA):
    curr_positive = True if A >= 0 else False
    if i == 0:
        last_positive = curr_positive
        continue

    abs_A = abs(A)
    if abs_A > max_absval:
        second_absval = max_absval
        arg2nd = argmax
        max_absval = abs_A
        argmax = i

    if not (last_positive & curr_positive):
        sep_indices.append(i)
        max_absvals.append(max_absval)
        argmaxes.append(argmax)
        second_absvals.append(second_absval)
        arg2nds.append(arg2nd)

        max_absval, second_absval = 0, None

# Last sep (DRY, a fucking code)
last_sep = sep_indices[-1]
last_AAA = AAA[last_sep:]
max_lastAAA = 0
argmax_lastAAA = 0
second_absval_lastAAA = None
arg2nd_lastAAA = None
for i, A in enumerate(last_AAA):
    abs_A = abs(A)
    if abs_A > max_lastAAA:
        second_absval_lastAAA = max_lastAAA
        arg2nd_lastAAA = argmax_lastAAA
        max_lastAAA = abs_A
        argmax_lastAAA = i + last_sep
sep_indices.append(N)
max_absvals.append(max_lastAAA)
argmaxes.append(argmax_lastAAA)
second_absvals.append(second_absval_lastAAA)
arg2nds.append(arg2nd_lastAAA)


# print(sep_indices, max_absvals, argmaxes, second_absvals, arg2nds)


# calc cost
for i, A in enumerate(AAA):
    cost = sum([2 * max_absval for max_absval in max_absvals])
    for j, sep in enumerate(sep_indices):
        sep_last = sep_indices[j - 1] if j != 0 else -1
        if sep - sep_last == 1:
            continue
        if sep_last <= i < sep:
            argmax = argmaxes[j]
            # Adjustment
            if argmax == i:
                cost -= 2 * max_absvals[j]
                cost += 2 * second_absvals[j]
        if sep <= i:
            break
    print(cost)
