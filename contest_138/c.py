# AC
N = int(input())
vvv = list(map(int, input().split()))
vvv.sort()

new_vvv = vvv
for _ in range(N - 1):
    merged = sum(new_vvv[:2]) / 2
    new_vvv = [merged] + new_vvv[2:]
    new_vvv.sort()

print(new_vvv[0])
