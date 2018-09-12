x = int(input())

max_result = 0
# Search b between 32 ** 2(lowest p) = 1024 
for b in range(1, 33):
    # Search p between 2~10 because 2(lowest b)^10 = 1024
    for p in range(2, 11):
        canditate = b**p
        if canditate <= x and canditate > max_result:
            max_result = canditate

print(max_result)