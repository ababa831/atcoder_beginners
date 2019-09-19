# AC
import sys
input_s = sys.stdin.readline

N, K = map(int, input_s().split())
xxx = list(map(int, input_s().split()))

min_elapsed_time = 10**10
for left, right in zip(xxx, xxx[K - 1:]):
    elapsed_time = right - left + min(abs(left), abs(right))
    """
    right - left : a section distance
    min(abs(left), abs(right)) : a start point to move the section
    """
    min_elapsed_time = \
        elapsed_time if elapsed_time < min_elapsed_time else min_elapsed_time

print(min_elapsed_time)
