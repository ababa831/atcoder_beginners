from math import log2

N = int(input())
if N % 2:
    search_lower = int(log2(abs(N) + 1))
else:
    search_upper = int(log2(abs(N)))

search_upper = search_lower + 1

# WIP