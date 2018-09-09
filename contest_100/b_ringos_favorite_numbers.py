# Wrong Answer:
# Some cases were wrong, but I could not detect them.
d, n = map(int, input().split())
print((100**d) * n)

# Consider the case: n = 100
# If n = 100, (100 ** d) * n -> 100 ** (d + 1) is correct
# So, in the situation, 
# you must change the calculation method: (100 ** d) * 101
"""
d, n = map(int, input().split())
if n == 100:    
    print((100**d) * (n+1))
else:
    print((100**d) * n)
"""