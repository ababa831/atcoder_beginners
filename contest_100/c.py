# WIP
import sys
sys_input = sys.stdin.readline
N = int(sys_input())
aaa = list(map(int, sys_input().split()))

# If all values are odd
aaa_remain = set(map(lambda x: x % 2, aaa))
if len(aaa_remain) == 1 and sum(aaa_remain) == 1:
    print(0)
    exit()

aaa_even = [a for a in aaa if a % 2 == 0]
target_a = max(aaa_even)

n_divide = 0
is_dividable = True
while is_dividable:
    is_dividable = False if target_a % 2 else True
    if is_dividable:
        target_a = target_a//2
        n_divide += 1

print(n_divide)
