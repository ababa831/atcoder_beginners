# Accepted
a, b = map(int, input().split())
s = input()

if len(s) != a + b + 1 or s[a] != "-":
    print("No")
elif "-" in s[:a] or "-" in s[a + 1:a + b + 1]:
    print("No")
else:
    print("Yes")