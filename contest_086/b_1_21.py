# Accepted
import math

ab = int(input().replace(" ", ""))
sqrt_ab = math.sqrt(ab)
if int(sqrt_ab) ** 2 == ab:
    print("Yes")
else:
    print("No")