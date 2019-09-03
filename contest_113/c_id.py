# WIP
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

py_list = [list(map(int, input().split()))+[i] for i, m in enumerate(range(m))]
py_list.sort(key=lambda x: x[1])

cursor_p = 1
current = 0
city = None
addresses = []
for py in py_list:
    p = py[0]
    y = py[1]
    idx = py[2]

    if p == cursor_p:
        current += 1
    elif p > cursor_p:
        current = 1
        cursor_p = p
    city = str(current).zfill(6)
    pref = str(cursor_p).zfill(6)

    addresses.append((idx, pref+city))

addresses.sort(key=lambda x: x[0])

for address in addresses:
    print(address[1])
