# WA: Someting Wrong (Too much memory)
k, a, b = map(int, input().split())

if b - a <= 1:
    print(k + 1)
else:
    remaining = k - (a - 1)
    if remaining <= 1:
        print(k + 1)
    else:
        biscket = a + (b - a)**int(remaining / 2)
        if remaining % 2:
            # Odd
            biscket += 1
        print(biscket)
