# AC
s = input()
K = int(input())

minimum_canditates = sorted(set(s))
n_counted = 0

canditates = []


def add_canditate(target_chara):
    global n_counted

    canditates.append(target_chara)
    n_counted += 1
    for c in minimum_canditates:
        next_target = target_chara + c
        if n_counted < K and next_target in s:
            add_canditate(next_target)


for c in minimum_canditates:
    add_canditate(c)

print(canditates[K - 1])
