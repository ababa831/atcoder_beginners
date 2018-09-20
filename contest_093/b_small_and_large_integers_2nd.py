# Accepted
a, b, k = map(int, input().split())
lower_list = [i for i in range(a, a + k)]
upper_list = [i for i in range(b, b - k, -1)]

out_list = sorted(set(lower_list + upper_list))
for out in out_list:
    if a <= out <= b:
        print(out)