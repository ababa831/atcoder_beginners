# Accepted, but too long codes.
s = sorted(input())
t = sorted(input(), reverse=True)
len_s = len(s)
len_t = len(t)
n_passed = 0

min_len = min(len_s, len_t)
for i in range(min_len):
    if s[i] < t[i]:
        print("Yes")
        exit()

if len_s < len_t:
    t = sorted(t)
    for i in range(len_s):
        if s[i] == t[i]:
            n_passed += 1
    if n_passed == len_s:
        print("Yes")
        exit()

print("No")