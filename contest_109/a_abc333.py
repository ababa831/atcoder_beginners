# Accepted
a, b = map(int, input().split())
for c in range(1, 4):
    if (a * b * c) % 2:
        print("Yes")
        exit()
print("No")