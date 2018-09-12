# Accepted
three_int = list(map(int, input().split()))
k = int(input())

for _ in range(k):
    three_int = sorted(three_int, reverse=True)
    # 0th element is the max value in the list (A, B, C)
    three_int[0] = three_int[0] * 2
print(sum(three_int))

# Another solution
# 1. Select max value: max(A, B, C)
# 2. Calculate others: A+B+C - max(A,B,C)
# 3. Double max(A, B, C) for K times: max(A, B, C) * 2^K
# 4. print(A+B+C - max(A,B,C) + max(A, B, C) * 2^K)
"""
a, b, c = map(int, input().split())
k = int(input())
print(a + b + c - max(a, b, c) + max(a, b, c) * 2**k)
"""