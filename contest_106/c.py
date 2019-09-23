# AC
S = input()
S_list = list(map(int, list(S)))
K = int(input())

S_set_under_K = set(S[:K])

if len(S) == 1:
    print(S)
elif len(S_set_under_K) == 1 and S_list[0] == 1:
    print(1)
else:
    for c in S:
        if c != "1":
            print(c)
            exit()
