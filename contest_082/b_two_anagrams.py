s = sorted(input())
t = sorted(input(), reverse=True)
len_s = len(s)
len_t = len(t)
n_passed = 0

for i in range(len_s):
    if s[i] < t[i]:
        print("Yes")
        exit()

t = sorted(t)
if len_s < len_t:
    for i in range(len_s):
        if s[i] == t[i]:
            n_passed += 1
    if n_passed == len_s:
        print("Yes")
        exit()
print("No")