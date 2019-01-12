# Accepted
import math

n = int(input())
h = int(input())
w = int(input())

remainder_row = n-h
remainder_col = n-w
total_row = remainder_row + 1
total_col = remainder_col + 1
combi_row = math.factorial(total_row) / math.factorial(remainder_row)
combi_col = math.factorial(total_col) / math.factorial(remainder_col)

print(int(combi_row * combi_col))
