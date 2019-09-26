from math import log2

N = int(input())
digit_canditate1 = int(log2(abs(N)))
digit_canditate2 = digit_canditate1 - 1

digit = None
if N < 0:
    digit = digit_canditate1 if digit_canditate1 % 2 else digit_canditate2
else:
    digit = digit_canditate2 if digit_canditate2 % 2 else digit_canditate1

ans_canditates = [[0, 0] for _ in range(2**digit)]
# {0, 1} * (-2) ** k + ...
# TODO: Calculation using DP
