# AC
# I coudn't explain why the logic works correctly
import sys

# Input
N = int(input())
aaa = list(map(int, sys.stdin.readline().split()))

sum_aaa = sum(aaa)

# Outout
print(sum_aaa - N)
