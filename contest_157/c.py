# WIP (WA)
import sys

sys_input = sys.stdin.readline

N, M = map(int, sys_input().split())
scsc = [tuple(map(int, sys_input().split())) for sc in range(M)]
s_mem = [0] * (N+1)

for i, (s, c) in enumerate(scsc):
    c_memorized = s_mem[s]
    if not c_memorized:
        s_mem[s] = c
        continue
    if c_memorized != c:
        print(-1)
        exit()

result = int(''.join(map(str, s_mem)))
if len(str(result)) != N:
    print(-1)
    exit()
print(result)
