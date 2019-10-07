# AC
import sys
import statistics

N = int(input())
AAA = list(map(int, sys.stdin.readline().split()))

AAA_minus_i = [A - (i+1) for i, A in enumerate(AAA)]
median_AAA_minus_i = round(statistics.median(AAA_minus_i))

ans = sum(list(map(lambda x: abs(x-median_AAA_minus_i), AAA_minus_i)))

print(ans)
