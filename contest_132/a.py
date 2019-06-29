S = input()

set_s = set(S)
if len(set_s) == 2:
    for val in set_s:
        if S.count(val) != 2:
            print('No')
            exit()
else:
    print('No')
    exit()

print('Yes')
             