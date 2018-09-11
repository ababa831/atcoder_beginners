# Accepted, But awkward thiking
# And, I searched how to appent a new value to set()
n = int(input())
s = input()


def get_common_chars(first_set, latter_set):
    common_chars = set([])
    for chara in first_set:
        if chara in latter_set:
            common_chars.add(chara)
    return common_chars


max_charlen = 0
for i in range(n - 1):
    first_set = set(s[:i + 1])
    latter_set = set(s[i + 1:])
    common_charlen = len(get_common_chars(first_set, latter_set))
    if max_charlen < common_charlen:
        max_charlen = common_charlen
print(max_charlen)