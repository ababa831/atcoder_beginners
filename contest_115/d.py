# In progress (Time out)
# May be WA
n, x = map(int, input().split())


def get_burger_size(l):
    return 1 + 2 * l


def get_harf_pcount(l):
    harf_p_count = 0
    for _ in range(l):
        harf_p_count = 2 * harf_p_count + 1
    return harf_p_count


burger_size = get_burger_size(n)
if x > int(burger_size / 2):
    harf_p_count = get_harf_pcount(n)
    if x <= burger_size - 2:
        pcount = harf_p_count + x - int(burger_size / 2) - 1
    else:
        pcount = harf_p_count + burger_size - 2 - int(burger_size / 2) - 1

print(pcount)