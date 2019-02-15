s = input()
n = 0
ans = 0
while n < 2**(len(s) - 1):
    p = 0
    for i in range(len(s) - 1):
        if n & (1 << i):
            ans += int(s[p:i + 1])
            p = i + 1
    if p < len(s):
        ans += int(s[p:])
    n += 1
print(ans)