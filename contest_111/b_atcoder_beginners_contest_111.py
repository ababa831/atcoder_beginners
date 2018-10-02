# Accepted, but shitty codes
n = int(input())

canditates = [111, 222, 333, 444, 555, 666, 777, 888, 999]
for i in range(len(canditates) - 1):
    if n < 111:
        print(111)
        exit()
    elif canditates[i] == n:
        print(n)
        exit()
    elif canditates[i] < n <= canditates[i + 1]:
        print(canditates[i + 1])
        exit()

# Another example (Shorter code)
"""
n = int(input())
if n % 111 == 0:
    print(n)
else:
    out = (n // 111 + 1) * 111
    print(out)
"""